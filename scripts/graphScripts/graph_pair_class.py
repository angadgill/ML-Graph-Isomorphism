__author__ = 'angad'

import networkx as nx
import random


class GraphPair(object):
    def __init__(self, graph1, graph2):
        self.graph1 = graph1
        self.graph2 = graph2
        self._is_isomorphic = nx.is_isomorphic(self.graph1, self.graph2)
        self.features = []

    def is_isomorphic(self):
        return self._is_isomorphic

    def add_feature(self, feature):
        self.features += [feature(self.graph1, self.graph2)]