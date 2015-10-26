import networkx as nx
import sys
sys.path.append('../../')
sys.path.append('../')

import dill as pickle

from graph_class import *

# THE ARGUMENTS FOR RUNNING THIS FILE ARE AS FOLLOWS:

# python generate_random_graphs.py (Type of Graph) (Number of Graphs) (Parameters for Graph Function)

# 'Type of Graph' is one of the following: 
    # 'small_world', 'small_world_newman', 'small_world_connected'
    # 'power_law', 'power_law_tree', 
    # 'random_graph', 'erdos_renyi_random'

# 'Number of Graphs' is an integer for batch generation

# 'Parameters for Graph Function' are the collection of parameters
    # required by the networkx function handles for random graph generation
    # documentation can be found: 
    # http://networkx.readthedocs.org/en/networkx-1.10/reference/generators.html

def main(argv):

    type_of_graph = argv[0]
    number_of_graphs = argv[1]
    parameters = argv[2:]

    arr = read_indices()

    cg.SWC = arr[0]
    cg.SWCC = arr[1]
    cg.SWNC = arr[2]
    cg.PLC = arr[3]
    cg.PLTC = arr[4]
    cg.RGC = arr[5]
    cg.ERRC = arr[6]

    # try:
    for i in range(0, int(number_of_graphs)):
        new_graph = RandomGraph(type_of_graph, parameters)
        graph = new_graph.graph
        name = new_graph.name_graph()
        path = new_graph.path

        save_graph(graph, name, path)
    #except:
        #print "An Error as occured, exiting before finishing..."

    write_indices([cg.SWC, 
                cg.SWCC, 
                cg.SWNC, 
                cg.PLC, 
                cg.PLTC, 
                cg.RGC, 
                cg.ERRC])



if __name__ == "__main__":
   main(sys.argv[1:])