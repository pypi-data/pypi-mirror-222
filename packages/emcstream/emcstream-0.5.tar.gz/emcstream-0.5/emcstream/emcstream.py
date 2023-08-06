import numpy as np
import sys
import umap
from sklearn.metrics import silhouette_score
from sklearn.metrics.cluster import adjusted_rand_score, contingency_matrix
from sklearn.cluster import KMeans
import datetime
from statistics import mean

import warnings
from emcstream.DataManager import DataManager
warnings.filterwarnings('ignore')


class EmCStream:
    def __init__(self, dataset_file_ath, labelsFilePath, horizon, k):
        self.datasetFilePath = dataset_file_ath
        self.labelsFilePath = labelsFilePath
        self.horizon = horizon
        self.k = k
        self.dataManager = DataManager(dataset_file_ath, labelsFilePath)
        self.data_length, self.feature_cnt = self.dataManager.data_shape()
        self.cluster_cnt = int(k)
        self.ari_drift_threshold = 1.0
        self.ari_threshold = 1.0
        self.ari_threshold_step = 0.001
        self.initial_ari_drift_threshold = self.ari_drift_threshold
        self.consecutiveDriftCnt = 0
        self.consecutive_no_drift_count = 0
        self.increaseDCPCnt = 4
        self.decreaseThreshold_DriftCnt = 4
        self.init_size = horizon * 2
        self.drift_check_period = horizon * 5
        self.initial_drift_check_period = self.drift_check_period
        self.match_fnx_size = 2 * horizon if horizon <= 5 * self.cluster_cnt else horizon
        self.detected_drift_count = 0
        self.total_embedding = np.empty(shape=[0, 2])
        self.total_k_labels = []
        self.total_t_labels = []
        self.total_X = np.empty(shape=[0, self.feature_cnt])
        self.no_more_data = False
        self.match_fnx = None
        self.drift_occured = False
        self.very_first_loop = True
        self.in_init_cycle = True
        self.aris = list()
        self.purity_list = list()
        self.siluet_list = list()
        self.f_size = 0
        self.max_ari_tobe_threshold = 0
        self.randomState1 = 1
        self.randomState2 = 1001
        self.verbose = 0

    def print_initial_parameters(self):
        print('init size: {}\nhorizon: {}'.format(self.init_size, self.horizon))  #
        print('drift check period : {}'.format(self.drift_check_period))
        print('overlap size : {}'.format(self.match_fnx_size))
        print('cluster count : {}'.format(self.cluster_cnt))
        print('initial ari_drift_threshold : {}'.format(self.ari_drift_threshold))
        print('\nExecuting EmCStream...\n')

    def purity_score(self, y_true, y_pred):
        con_mat = contingency_matrix(y_true, y_pred)
        return float(np.sum(np.amax(con_mat, axis=0))) / float(np.sum(con_mat))

    def run(self):
        self.print_initial_parameters()
        while not self.no_more_data:
            self.embedding = None
            self.in_init_cycle = True
            self.X, self.tlabels = self.dataManager.get_data(self.init_size)
            if self.X is False:
                print('breaking the loop because X is false, which means no more data.')
                break
            self.reducer = umap.UMAP(random_state=self.randomState1)
            self.randomState1 = self.randomState1 + 1
            self.embedding = self.reducer.fit_transform(self.X)
            self.added_X = self.X
            self.added_tlabels = self.tlabels
            self.drift_occured = False
            while not self.drift_occured and not self.no_more_data:
                self.added_instance_cnt = 0
                self.drift_check_time = False
                while not self.drift_check_time and not self.no_more_data:
                    self.X, self.tlabels = self.dataManager.get_data(self.horizon)
                    if self.X is False:
                        self.no_more_data = True
                        if self.verbose:
                            print('setting no_more_data to true.')
                        break
                    self.embedding = np.append(self.embedding, self.reducer.transform(self.X), axis=0)
                    self.added_X = np.append(self.added_X, self.X, axis=0)
                    self.added_tlabels = np.append(self.added_tlabels, self.tlabels)
                    self.added_instance_cnt += self.horizon
                    if self.added_instance_cnt >= self.drift_check_period:
                        self.drift_check_time = True

                if not self.no_more_data:
                    if self.verbose:
                        print('calculation kmeans on this window, with k={}'.format(self.cluster_cnt))
                        print('reinitialize umap with last [{}] data instances, to check for concept drift.'.format(
                            self.added_instance_cnt))
                    self.check_drift()
                else:
                    self.finalize()
                    break
                self.embedding = np.empty(shape=[0, 2])
                self.added_X = np.empty(shape=[0, self.feature_cnt])
                self.added_tlabels = np.empty(shape=[0, 1])
                self.klabels = []
                if not self.drift_occured:
                    self.dataManager.iterate_index(-self.match_fnx_size)

                self.in_init_cycle = False
        print('\n\n-\n--\n---\nExecution completed:')
        if self.verbose:
            print('total embedding : [{}]'.format(self.total_embedding.shape))
            print('total klabels : [{}]'.format(len(self.total_k_labels)))
            print('total tlabels : [{}]'.format(self.total_t_labels.shape))
            print('total X : [{}]'.format(self.total_X.shape))
        ari = adjusted_rand_score(self.total_k_labels, self.total_t_labels)
        pur = self.purity_score(self.total_k_labels, self.total_t_labels)
        sil = silhouette_score(self.total_X, self.total_k_labels)
        self.print_results(ari, pur, sil)
        sys.exit(0)

    def print_results(self, ari, pur, sil):
        print('\nari of total calculation is [{}]'.format(ari))
        print('average ari of total [{}] chunks is [{}]'.format(len(self.aris), mean(self.aris)))
        print('\npurity of total calculation is [{}]'.format(pur))
        print('average purity of total [{}] chunks is [{}]'.format(len(self.purity_list), mean(self.purity_list)))
        print('\nsilhouette_score of total calculation is [{}]'.format(sil))
        print('average silhouette_score of total [{}] chunks is [{}]'.format(len(self.siluet_list),
                                                                             mean(self.siluet_list)))
        print('\ndetected drift count is [{}]'.format(self.detected_drift_count))

    def check_drift(self):
        kmeans = KMeans(n_clusters=self.cluster_cnt, random_state=0).fit(self.embedding)
        self.klabels = [x for x in kmeans.labels_]
        self.new_reducer = umap.UMAP(random_state=self.randomState2)
        self.randomState2 = self.randomState2 + 1
        self.new_embedding = self.new_reducer.fit_transform(self.added_X)
        self.new_kmeans = KMeans(n_clusters=self.cluster_cnt, random_state=0).fit(self.new_embedding)
        self.new_klabels = [x for x in self.new_kmeans.labels_]

        if not self.very_first_loop:
            self.create_match_fnx()
            self.convert_labels()

        self.ari = adjusted_rand_score(self.klabels, self.new_klabels)
        if self.ari >= self.ari_drift_threshold:
            self.handle_no_drift()
        else:
            self.handle_drift()

    def create_match_fnx(self):
        self.prev_tomatch = self.total_k_labels[-self.match_fnx_size:]
        self.curr_tomatch = self.klabels[:self.match_fnx_size]
        self.match = np.zeros(shape=[self.cluster_cnt, self.cluster_cnt])
        self.match_fnx = np.zeros(shape=[self.cluster_cnt])
        for i in range(self.match_fnx_size):
            self.match[int(self.curr_tomatch[i]), int(self.prev_tomatch[i])] += 1
        for i in range(self.cluster_cnt):
            self.match_fnx[i] = np.argmax(self.match[i])

    def convert_labels(self):
        if self.verbose:
            print('---+---+---+---')
            print(self.match)
            print('---')
            print(self.match_fnx)
            print('---+---+---+---')
        for i in range(len(self.klabels)):
            self.klabels[i] = self.match_fnx[self.klabels[i]]

    def handle_no_drift(self):
        self.max_ari_tobe_threshold = 0
        true_ari = adjusted_rand_score(self.klabels, self.added_tlabels)
        purity = self.purity_score(self.klabels, self.added_tlabels)
        try:
            siluet = silhouette_score(self.added_X, self.klabels)
            print("Successfully calculated silhoutte score")
            print(len(self.added_X), len(self.klabels), self.f_size)
            self.f_size += len(self.added_X)
            print(f"Silhoutte score: {silhouette_score(self.added_X, self.klabels)}")
            self.aris.append(true_ari)
            self.purity_list.append(purity)
            self.siluet_list.append(siluet)
        except Exception as e:
            self.f_size += len(self.added_X)
            print(f"Exception occured while calculating silhoutte score: {e}")
            print(len(self.added_X), len(self.klabels), self.f_size)

        if self.verbose:
            print('no concept drift yet [{}]'.format(self.ari))
        self.consecutiveDriftCnt = 0
        self.consecutive_no_drift_count = self.consecutive_no_drift_count + 1
        if self.consecutive_no_drift_count >= self.increaseDCPCnt:
            self.consecutive_no_drift_count = 0
            if self.drift_check_period < self.initial_drift_check_period:
                self.drift_check_period = self.drift_check_period + self.horizon
                if self.verbose:
                    print('new drift check period (increased) is [{}]'.format(self.drift_check_period))

        self.ari_drift_threshold = self.ari - self.ari_threshold_step
        if self.verbose:
            print('new ari drift threshold (increased) is [{}]'.format(self.ari_drift_threshold))

        if self.very_first_loop:
            self.total_embedding = np.append(self.total_embedding, self.embedding, axis=0)
            self.total_k_labels = self.total_k_labels + self.klabels
            self.total_t_labels = np.append(self.total_t_labels, self.added_tlabels)
            self.total_X = np.append(self.total_X, self.added_X, axis=0)
            self.very_first_loop = False
        else:
            self.total_embedding = np.append(self.total_embedding, self.embedding[self.match_fnx_size:], axis=0)
            self.total_k_labels = self.total_k_labels + self.klabels[self.match_fnx_size:]
            self.total_t_labels = np.append(self.total_t_labels, self.added_tlabels[self.match_fnx_size:])
            self.total_X = np.append(self.total_X, self.added_X[self.match_fnx_size:], axis=0)
        if self.verbose:
            print('total embedding : [{}]'.format(self.total_embedding.shape))
            print('total klabels : [{}]'.format(len(self.total_k_labels)))
            print('total tlabels : [{}]'.format(self.total_t_labels.shape))
            print('total X : [{}]'.format(self.total_X.shape))

    def handle_drift(self):
        self.drift_occured = True
        self.consecutive_no_drift_count = 0
        if self.in_init_cycle:
            self.consecutiveDriftCnt += 1
            if self.ari > self.max_ari_tobe_threshold:
                self.max_ari_tobe_threshold = self.ari
            if self.verbose:
                print('***** a consecutive concept drift detected.*****[{}]'.format(self.ari))
            self.dataManager.iterate_index(-(self.added_instance_cnt + self.init_size))
            if self.drift_check_period > self.match_fnx_size + self.horizon:
                self.drift_check_period = self.drift_check_period - self.horizon
                if self.verbose:
                    print('new drift check period (decreased) is [{}]'.format(self.drift_check_period))
            elif self.consecutiveDriftCnt >= self.decreaseThreshold_DriftCnt:
                # self.ari_drift_threshold = self.max_ari_tobe_threshold - self.ari_threshold_step
                self.ari_drift_threshold = self.max_ari_tobe_threshold - self.ari_threshold_step
                self.max_ari_tobe_threshold = 0
                if self.verbose:
                    print('new ari drift threshold (decreased) is [{}]'.format(self.ari_drift_threshold))
                self.consecutiveDriftCnt = 0
        else:
            if self.verbose:
                print('********** a new concept drift detected.**********[{}]'.format(self.ari))
            print("Prev_index", self.dataManager.current_index)
            self.dataManager.iterate_index(-self.added_instance_cnt)
            print("Current_index", self.dataManager.current_index)
            self.detected_drift_count += 1

    def finalize(self):
        if self.verbose:
            print('calculating kmeans on this window, with k={}'.format(self.cluster_cnt))
        self.kmeans = KMeans(n_clusters=self.cluster_cnt, random_state=0).fit(self.embedding)
        self.klabels = [x for x in self.kmeans.labels_]
        self.create_match_fnx()
        if self.verbose:
            print('---+---+---+---')
            print(self.match)
            print('---')
            print(self.match_fnx)
            print('---+---+---+---')
        self.convert_labels()
        self.total_embedding = np.append(self.total_embedding, self.embedding[self.match_fnx_size:], axis=0)
        self.total_k_labels = self.total_k_labels + self.klabels[self.match_fnx_size:]
        self.total_t_labels = np.append(self.total_t_labels, self.added_tlabels[self.match_fnx_size:])
        self.total_X = np.append(self.total_X, self.added_X[self.match_fnx_size:], axis=0)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print('\nusage: python EmCStream.py datasetFilePath labelsFilePath horizon k\n')
        sys.exit(1)

    print('----- new run at : {} -----'.format(datetime.datetime.now().isoformat()))
    print("Running EmCStream on " + sys.argv[1])

    emcstream = EmCStream(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    emcstream.run()

