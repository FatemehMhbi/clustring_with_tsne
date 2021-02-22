# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:53:28 2020

@author: Fatemeh
The sequences must be the same size.
"""

from Bio import SeqIO
from Bio.Seq import Seq
import os, sys, re
import pandas as pd
import numpy as np


def fasta_to_mat(fasta_file):
    """converts a fasta file to csv file, each row is nomarical representation of each seq,
    A->1, C->2, G->3, T->4, - ->5"""
    df = pd.DataFrame()
    records = list(SeqIO.parse(fasta_file, "fasta"))
    for record in records:
        searchObj = re.finditer(r"[^ATGC]", str(record.seq))  
        for m in searchObj:
            pos = m.start()
            record = record[:pos] + '-' + record[pos+1:]
        seq_of_int = str(record.seq).replace('A', '1').replace('C', '2').replace('G', '3').replace('T','4').replace('-', '5')
        record.seq = Seq(seq_of_int)
        print(record.id)
        try:
            df[str(record.id)] = list(map(int, list(seq_of_int))) 
        except:
            continue
    return df.T
    

def gaps_to_null(df):
    """replace 5 in the dataframe with null"""
    df = df.replace(5, np.nan)
    # pd.DataFrame(df).to_csv("_5_removed.csv") 
    return df


def remove_columns_with_gap(df, gap_no):
    """removes all the columns that have more than gap_no number of gaps"""
    for column in df.columns:
        counts = df.pivot_table(index=[column], aggfunc='size')
        if (df.shape[0] - sum(list(counts))) >= gap_no:
            df.drop(column, inplace=True, axis=1)
    return df
    

if __name__ == '__main__':
    file = sys.argv[1]
    mat = fasta_to_mat(file)
    mat.to_csv(file.split(".fasta")[0] + "_as_matrix.csv")    