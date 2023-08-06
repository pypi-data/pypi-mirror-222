from setuptools import setup, find_packages

setup(
    name='emcstream',
    version='0.1',
    url='https://gitlab.com/alaettinzubaroglu/emcstream',
    author='Alaettin Zubaroğlu',
    author_email='alaettinzubaroglu@gmail.com',
    description='A python implementation for online embedding and clustering of evolving data streams',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'umap-learn',
        'sklearn',
        'statistics',
        'pandas'
    ],
)
