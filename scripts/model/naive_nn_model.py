__author__ = 'angad'

'''
This implements and tests a naive neural network model to determine if two graphs are isomorphic
Input to the neural network are the features used in the naive_model
'''

import networkx as nx
import random
import numpy as np

from scripts.model import features
from scripts.model import graph_pair_class
from scripts.model import permute_graph
from scripts.graphScripts import ping

from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import SGD


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


'''Neural Network model'''
X = np.array([g.features for g in graphPairs])
y = np.array([g.is_isomorphic for g in graphPairs])
shuffle = range(len(y))
random.shuffle(shuffle)
X = X[shuffle]
y = y[shuffle]

model = Sequential()
model.add(Dense(output_dim=10, input_dim=6, activation='relu'))
model.add(Dense(output_dim=1, activation='sigmoid'))
sgd = SGD()
model.compile(optimizer=sgd, loss='mean_absolute_error')

model.fit(X, y, nb_epoch=20, verbose=2, validation_split=0.2, show_accuracy=True)
