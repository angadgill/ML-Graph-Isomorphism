# Creates Pair of Isospectral Non-isomorphic Graphs (PING)
# Must provide a valid degree (d) and nodes (n)
# Degree must be at most (n-1)
# Nodes must be a multiple of 2

import networkx as nx
# import random #Standard random library seems to get stuck in a pattern, numpy doesn't
from numpy import random
from math import factorial


def create(degree, nodes):
    # Returns a pair of PING
    if degree > nodes - 1:
        print "Error: Degree must be at most (nodes-1)"
        return 0
    if nodes % 2 != 0:
        print "Error: Nodes must be a multiple of 2"
        return 0

    node_list = range(nodes)

    for _ in xrange(factorial(nodes)):
        random.shuffle(node_list)

        # Generate first PING graph
        seed = 1
        g1 = nx.random_regular_graph(degree, nodes, seed=seed)
        g2 = nx.random_regular_graph(degree, nodes, seed=seed)
        for new_node in [nodes + 1, nodes + 2]:
            g1.add_node(new_node)
            g2.add_node(new_node)
            for connect_to_node in node_list[:nodes/2]:
                g1.add_edge(new_node, connect_to_node)
            for connect_to_node in node_list[nodes/2:]:
                g2.add_edge(new_node, connect_to_node)
        if not nx.is_isomorphic(g1, g2):
            return g1, g2

    if nx.is_isomorphic(g1, g2):
        print "Error: Cannot create a PING for this combination of degree and nodes"
        return 0

    return g1, g2
