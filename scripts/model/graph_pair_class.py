__author__ = 'angad'

from scripts.model.features import *
from matplotlib import pyplot as plt
import networkx as nx

class GraphPair(object):
    def __init__(self, graph1, graph2):
        self.graph1 = graph1
        self.graph2 = graph2
        self.is_isomorphic = nx.is_isomorphic(self.graph1, self.graph2)
        self.features = []

    def add_feature(self, feature):
        self.features += [feature(self.graph1, self.graph2).get_value()]

    def draw(self):
        plt.subplot(1,2,1)
        nx.draw(self.graph1)
        plt.subplot(1,2,2)
        nx.draw(self.graph2)

