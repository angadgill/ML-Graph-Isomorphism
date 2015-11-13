__author__ = 'angad'

# This implements and tests a naive machine learning algorithm to determine if two graphs are isomorphic

import networkx as nx
import random

from scripts.model import features
from scripts.model import graph_pair_class
from scripts.model import permute_graph
from scripts.graphScripts import ping

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import ShuffleSplit


# List of features used in this model
feature_list = [features.CompareNumOfNodes, features.CompareNumOfEdges, features.CompareDirected,
                features.CompareDegreeDistribution, features.CompareLSpectrum, features.CompareASpectrum]

# All graph pairs are contained in this list
graphPairs = []

# Base graph for all isomorphic graphs
g_base_nodes = 10
g_base = nx.watts_strogatz_graph(g_base_nodes, 5, 0.1)

# Create a list of isomorphic graph pairs
print "Creating list of isomorphic graph pairs..."
for _ in xrange(100):
    g = permute_graph.permute_graph(g_base, random.randint(1,g_base_nodes))
    graphPair = graph_pair_class.GraphPair(g_base, g)
    for f in feature_list:
        graphPair.add_feature(f)
    graphPairs += [graphPair]
print "Done!"

# Create a list of random graph pairs
print "Creating list of random graph pairs..."
for _ in xrange(100):
    g = nx.watts_strogatz_graph(g_base_nodes, 5, 0.1)
    graphPair = graph_pair_class.GraphPair(g_base, g)
    for f in feature_list:
        graphPair.add_feature(f)
    graphPairs += [graphPair]
print "Done!"

# Create a list of PING graphs
print "Creating PING graphs..."
for _ in xrange(100):
    g1, g2 = ping.create(2,10)
    graphPair = graph_pair_class.GraphPair(g1,g2)
    for f in feature_list:
        graphPair.add_feature(f)
    graphPairs += [graphPair]
print "Done!"

# Convert graphPairs to a Pandas dataframe
data = [g.features + [g.is_isomorphic] for g in graphPairs]
columns = ['feature_'+str(x) for x in range(len(feature_list))]+['is_isomorphic']
data = pd.DataFrame(data, columns=columns)

# Train model on random samples

model = LogisticRegression()
split = ShuffleSplit(data.shape[0], n_iter=3, test_size=0.2)
scores = []

print "Training and testing model..."
for fit_split, test_split in split:
    model.fit(data.loc[fit_split, columns[:-1]], data.loc[fit_split, columns[-1]])
    scores += [model.score(data.loc[test_split, columns[:-1]], data.loc[test_split, columns[-1]])]
print "Done!"
print "Fit scores:", str(scores)
