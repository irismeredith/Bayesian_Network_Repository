# This script generates summary plots for publication from the analysis performed in the other filed using Seaborn.

# Author: Iris Meredith

# Last modified: 31/05/2021

# Imports

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import bnlearn

import pickle

# Load the data

brisbane_trip_data = pd.read_csv('training_data.csv')

synthetic_data = pd.read_csv('generated_sample.csv')

# Filter the data to eliminate overly long trips

brisbane_trip_data_truncated = brisbane_trip_data.loc[brisbane_trip_data['Duration'] < 10000]

synthetic_data_truncated = synthetic_data.loc[synthetic_data['Duration'] < 10000]


# Configure plotting window

sns.set(style='whitegrid', palette='deep', font_scale=1.1, rc={"figure.figsize": [8, 5]})

# Duration Plots

plot = sns.distplot(brisbane_trip_data['Tag_on_minute'], kde=True,
                    hist_kws={"alpha": 1}).set(xlabel='Trip Duration', ylabel='Count')

plt.show()

plot = sns.distplot(synthetic_data['Tag_on_minute'], kde=True,
                    hist_kws={"alpha": 1}).set(xlabel='Trip Duration', ylabel='Count')

plt.show()

plot = sns.distplot(brisbane_trip_data_truncated['Tag_on_minute'], kde=True,
                    hist_kws={"alpha": 1}).set(xlabel='Trip Duration', ylabel='Count')

plt.show()

plot = sns.distplot(synthetic_data_truncated['Tag_on_minute'], kde=True,
                    hist_kws={"alpha": 1}).set(xlabel='Trip Duration', ylabel='Count')

plt.show()

# Read in the various graphs that have been learned and print them out

# infile = open('Learned_graph.p', 'rb')

# G = pickle.load(infile)

# infile.close()

# bnlearn.plot(G)


infile = open('Learned_graph_HC.p', 'rb')

G = pickle.load(infile)

infile.close()

bnlearn.plot(G)


# infile = open('Fitted_model.p', 'rb')

# G = pickle.load(infile)

# infile.close()

# bnlearn.plot(G)
