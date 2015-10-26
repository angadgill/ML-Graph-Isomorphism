import networkx as nx
import dill as pickle

SWC = 0
SWCC = 0
SWNC = 0
PLC = 0
PLTC = 0
RGC = 0
ERRC = 0


# small_world_count = SWC
# small_world_connected_count = SWCC
# small_world_newman_count = SWNC
# power_law_count = PLC
# power_law_tree_count = PLTC
# random_graph_count = RGC
# erdos_renyi_random_count = ERRC

class RandomGraph(object):


    def __init__(self, type_of_graph, params):
        self.type = type_of_graph
        self.create_graph(params)
        self.params = params

    def create_graph(self, params):

        global SWC
        global SWCC
        global SWNC
        global PLC
        global PLTC
        global RGC
        global ERRC

        # case statements on type of graph

        if self.type == 'small_world':
            self.graph = nx.watts_strogatz_graph(int(params[0]), int(params[1]), float(params[2]), None if len(params) < 4 else int(params[3]))
            SWC += 1
            print SWC
            self.idx = SWC
            self.path = 'smallWorldGraphs'
        elif self.type == 'small_world_connected':
            self.graph = nx.connected_watts_strogatz_graph(int(params[0]), int(params[1]), float(params[2]), 100 if len(params) < 4 else int(params[3]), None if len(params) < 5 else int(params[4]))
            SWCC += 1
            self.idx = SWCC
            self.path = 'smallWorldConnectedGraphs'
        elif self.type == 'small_world_newman':
            self.graph = nx.newman_watts_strogatz_graph(int(params[0]), int(params[1]), float(params[2]), None if len(params) < 4 else int(params[3]))
            SWNC += 1
            self.idx = SWNC
            self.path = 'smallWorldNewmanGraphs'
        elif self.type == 'power_law':
            self.graph = nx.powerlaw_cluster_graph(int(params[0]), int(params[1]), float(params[2]), None if len(params) < 4 else int(params[3]))
            PLC += 1
            self.idx = PLC
            self.path = 'powerLawGraphs'
        elif self.type == 'power_law_tree':
            self.graph = nx.random_powerlaw_tree(int(params[0]), 3 if len(params) < 2 else float(params[1]), None if len(params) < 3 else int(params[2]), 100 if len(params) < 4 else int(params[3]))
            PLTC += 1
            self.idx = PLTC
            self.path = 'powerLawTreeGraphs'
        elif self.type == 'random_graph':
            self.graph = nx.gnm_random_graph(int(params[0]), int(params[1]), None if len(params) < 3 else int(params[2]), False if len(params) < 4 else bool(params[3]))
            RGC += 1
            self.idx = RGC
            self.path = 'randomGraphs'
        elif self.type == 'erdos_renyi_random':
            self.graph = nx.erdos_renyi_graph(int(params[0]), float(params[1]), None if len(params) < 3 else int(params[2]), False if len(params) < 4 else bool(params[3]))
            ERRC += 1
            self.idx = ERRC
            self.path = 'erdosRenyiRandomGraphs'
        else:
            print 'GRAPH TYPE:', self.type
            raise Exception('Invalid Type of Graph input into argv[2]')

    def params_string(self):
        ret_str = ''
        for i in range(0, len(self.params) - 1):
            ret_str = ret_str + self.params[i]
            ret_str = ret_str + '_'
        ret_str = ret_str + self.params[-1]
        return ret_str

    def name_graph(self):
        params_string = self.params_string()
        return self.type + '___' + str(self.idx) + '___params_' + params_string + '.p'

def save_graph(graph, name, path):
    f = open('../../graphs/' + path + '/' + name, 'w')
    pickle.dump(graph, f)
    f.close()

def read_indices():
    f = open('../../graphs/graph_indices.p', 'r')
    return pickle.load(f)

def write_indices(arr):
    f = open('../../graphs/graph_indices.p', 'w')
    pickle.dump(arr, f)
    f.close()