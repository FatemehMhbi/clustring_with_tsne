# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:43:26 2021

@author: Fatemeh
"""

from convert_seq_to_mat import fasta_to_mat
from clustring_with_tsne import clustring
import sys, os

os.chdir("C:/Users/Fatemeh/Dropbox/corona/msa_1004/")

if __name__ == '__main__':
    fasta_file = 'cluster_4/example_aligned_to_ref.fasta' #sys.argv[1]
    seqs_as_mat = fasta_to_mat(fasta_file)
    labeling = clustring(seqs_as_mat, 2, 4)
    labeling.to_csv(fasta_file.split('.csv')[0] + '_kmeans_labels.csv')