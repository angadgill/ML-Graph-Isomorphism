__author__ = 'angad'

from scripts.model.features import *

class GraphPair(object):
    def __init__(self, graph1, graph2):
        self.graph1 = graph1
        self.graph2 = graph2
        self.is_isomorphic = nx.is_isomorphic(self.graph1, self.graph2)
        self.features = []

    def add_feature(self, feature):
        self.features += [feature(self.graph1, self.graph2).get_value()]
