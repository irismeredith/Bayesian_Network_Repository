# This script uses bnlearn to fit parameters to a previously learned or defined Bayesian network structure

# Author: Iris Meredith

# Last modified: 29/05/2021

import pandas as pd

import bnlearn

import pickle

# Load the training data

training_data = pd.read_csv('training_data.csv')

# Infuriatingly enough, using a larger sample tends to blow out my device's memory

training_data = training_data.sample(n=10000)

# Load the graph structure

infile = open('Learned_graph_HC.p', 'rb')

G = pickle.load(infile)

infile.close()

# Fit the model and store it

fitted_model = bnlearn.parameter_learning.fit(G, training_data)

filename = 'Fitted_model.p'

outfile = open(filename, 'wb')

pickle.dump(fitted_model, outfile)

outfile.close()
