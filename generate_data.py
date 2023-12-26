# This script generates samples from a fitted Bayesian Network model

# Author: Iris Meredith

# Last modified: 27/12/2023

# Imports

import bnlearn

import pickle

# Load model

infile = open('Fitted_model.p', 'rb')

G = pickle.load(infile)

infile.close()

# Generate samples from the loaded model

sample_frame = bnlearn.sampling(G, n=100000)

# Print a few data points and dump the generated data to a csv

print(sample_frame.head(3))

sample_frame.to_csv('generated_sample.csv', index_label='Trip_ID')
