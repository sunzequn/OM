import networkx as nx
from itertools import product

threshold = 0.6


def sim_graph(sim_mat, source_uri_prefix='s', target_uri_prefix='t'):
    row = sim_mat.shape[0]
    col = sim_mat.shape[1]
    graph = nx.Graph()
    for i, j in product(range(row), range(col)):
        if sim_mat[i, j] > threshold:
            graph.add_edge(splice(source_uri_prefix, i), splice(target_uri_prefix, j), weight=sim_mat[i, j])
    return graph


def splice(prefix, index):
    return prefix + "_" + str(index)


def mwgm(graph, source_uri_prefix='s'):
    edges = nx.max_weight_matching(graph, maxcardinality=True)
    print(len(edges))
    matching_pairs = []
    keys = [k for k in edges.keys() if k.startswith(source_uri_prefix)]
    for key in keys:
        matching_pairs.append((key, edges[key]))
    return matching_pairs
