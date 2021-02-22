# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:43:26 2021

@author: Fatemeh
"""

from convert_seq_to_mat import fasta_to_mat
from clustring_with_tsne import clustring
import sys, os


if __name__ == '__main__':
    fasta_file = sys.argv[1]
    n_clusters = sys.argv[2]
    pca_n_components = sys.argv[3]
    seqs_as_mat = fasta_to_mat(fasta_file)
    labeling = clustring(seqs_as_mat, n_clusters, pca_n_components)
    labeling.to_csv(fasta_file.split('.csv')[0] + '_kmeans_labels.csv')