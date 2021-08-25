# This script performs shape learning of Bayesian Networks using bnlearn and one's choice of algorithm

# Author: Iris Meredith

# Last modified: 27/05/2021

import pandas as pd

import bnlearn

import pickle

training_data = pd.read_csv('training_data.csv', index_col='Trip_ID')

print(training_data.columns)

training_data = training_data.sample(50000)

# Learn the best structure for the network: method flags are 'hc' for Hill Climbing and 'cs' for constraint search

model = bnlearn.structure_learning.fit(training_data, methodtype='hc')

# Pickle the learned structure

filename = 'Learned_graph_HC.p'

outfile = open(filename, 'wb')

pickle.dump(model, outfile)

outfile.close()
