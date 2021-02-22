# clustring_with_tsne
This code reads the sequences out of the input fasta file and converts them into numarical respresentations. A, C, T, and G in each DNA sequence is replaced by 1, 2, 3, and 4 respectively (gaps are replaced by 5). This numarical representation is returned and saved as a matrix (a dataframe in which each row is one sequence). \
The matrix then passed to PCA in order to reduce the dimensionality of data.
Then reduced data is passed to t-SNE, which converts data to points in 2D. And finally the datapoints are clustered using kMeans clustring. \
The number of PCA components and the number of clusters in the final clustering needs to be specifiend. For sequences 50 as the number of PCA componenets usually works the best. \
Output is saved as a csv file, which contains sequence ids and their labelings. 

# How to run:
python3.7 clustring_seqs.py example_input.fasta n_clusters n_pca_components

Here n_clusters is the number of the clusters and n_pca_components is the number of PCA componenets.
