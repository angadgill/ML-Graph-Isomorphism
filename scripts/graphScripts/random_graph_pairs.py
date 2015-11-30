
import networkx as nx
import random
import pickle

from scripts.model import features
from scripts.model import graph_pair_class
from scripts.model import permute_graph
from scripts.graphScripts import ping

# List of features used in this model
feature_list = [features.CompareNumOfNodes, features.CompareNumOfEdges, features.CompareDirected,
                features.CompareDegreeDistribution, features.CompareLSpectrum, features.CompareASpectrum]

# All graph pairs are contained in this list
graphPairs = []

nodes = 10
num_of_graphs = 100

# Base graph for all isomorphic graphs
g_base_nodes = nodes+1
g_base = nx.watts_strogatz_graph(g_base_nodes, 5, 0.1)

# Create a list of isomorphic graph pairs
print "Creating list of isomorphic graph pairs..."
for _ in xrange(num_of_graphs):
    g = permute_graph.permute_graph(g_base, random.randint(1,g_base_nodes))
    graphPair = graph_pair_class.GraphPair(g_base, g)
    for f in feature_list:
        graphPair.add_feature(f)
    graphPairs += [graphPair]
print "Done!"

# Create a list of random graph pairs
print "Creating list of random graph pairs..."
for _ in xrange(num_of_graphs):
    g = nx.watts_strogatz_graph(g_base_nodes, 5, 0.1)
    graphPair = graph_pair_class.GraphPair(g_base, g)
    for f in feature_list:
        graphPair.add_feature(f)
    graphPairs += [graphPair]
print "Done!"

# Create a list of PING graphs
print "Creating PING graphs..."
for _ in xrange(num_of_graphs):
    g1, g2 = ping.create(int(nodes/5),nodes)
    graphPair = graph_pair_class.GraphPair(g1,g2)
    for f in feature_list:
        graphPair.add_feature(f)
    graphPairs += [graphPair]
print "Done!"

print "Pickling graphs"
filename = 'graphPairs_' + str(nodes) + '_nodes_' + str(len(graphPairs)) + '_pairs.bro'
f = open(filename, 'wb')
pickle.dump(graphPairs, f)
f.close()
print "Done!"
