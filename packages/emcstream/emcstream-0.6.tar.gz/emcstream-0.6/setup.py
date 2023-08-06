from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='emcstream',
    version='0.6',
    url='https://gitlab.com/alaettinzubaroglu/emcstream',
    author='Alaettin Zubaroğlu',
    author_email='alaettinzubaroglu@gmail.com',
    description='A python implementation for online embedding and clustering of evolving data streams',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'umap-learn',
        'scikit-learn',
        'statistics',
        'pandas'
    ],
)
