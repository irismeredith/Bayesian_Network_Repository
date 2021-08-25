# This script generates samples from a fitted Bayesian Network model

# Author: Iris Meredith

# Last modified

import bnlearn

import pickle

infile = open('Fitted_model.p', 'rb')

G = pickle.load(infile)

infile.close()

sample_frame = bnlearn.sampling(G, n=100000)

print(sample_frame.head(3))

sample_frame.to_csv('generated_sample.csv', index_label='Trip_ID')
