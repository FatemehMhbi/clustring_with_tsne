# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:11:34 2020

@author: Fatemeh
"""

from sklearn.manifold import TSNE
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import decomposition
import sys


def T_SNE_kmeans(dist_mat, n_clusters):
    """applies t_SNE on input df which reduces dimensionality to 2 (each row a sample), 
    then using kMeans datapoints are clustered into n_clusters"""
    print("running TSNE...")
    TSNE_result = TSNE(learning_rate = 50).fit_transform(dist_mat)
    df = pd.DataFrame()
    df['x'] = TSNE_result[:,0]
    df['y'] = TSNE_result[:,1]
    kmeans = KMeans(n_clusters = n_clusters, random_state = 0).fit(df)
    kmeans_labels = pd.DataFrame({'kmeans_labels': kmeans.labels_ }, index=dist_mat.index)
    print("Done!")
    return kmeans_labels


def PCA(X, n_components):
    """applies PCA on the input df which reduces dimensionality to n_components"""
    print("running PCA...")
    pca = decomposition.PCA(n_components = n_components)
    pca.fit(X)
    X_reduced = pca.transform(X)
    return X_reduced


def clustring(input_mat, n_clusters, n_pca_components):
    """returns TSNE_kmeans clustrings' labels"""
    input_ = pd.DataFrame(PCA(input_mat, n_pca_components), index = input_mat.index)
    kmeans_labels = T_SNE_kmeans(input_, n_clusters)
    return kmeans_labels


if __name__ == '__main__':
    file = sys.argv[1]
    input_mat = pd.read_csv(file)
    input_mat = input_mat.set_index(input_mat.columns[0])
    labeling = clustring(input_mat, 13)
    labeling.to_csv(file.split('.csv')[0] + '_kmeans_labels.csv')