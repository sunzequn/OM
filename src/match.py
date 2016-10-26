import networkx as nx
from itertools import product

nx.Graph().__len__()


def pairwise(sim_mat, threshold, source_uri_prefix='s', target_uri_prefix='t'):
    print('threshold : %f' % threshold)
    matching_pairs = []
    for i, j in product(range(sim_mat.shape[0]), range(sim_mat.shape[1])):
        if sim_mat[i, j] > threshold:
            matching_pairs.append((str_splice(source_uri_prefix, i), str_splice(target_uri_prefix, j)))
    return matching_pairs


#
# def mwgm_level(sim_mat, *threshold, remove='node', source_uri_prefix='s', target_uri_prefix='t'):
#     print('threshold :', threshold)
#     matching_pairs_dict = {}
#     for th in threshold:
#         graph = sim_graph(sim_mat, th, source_uri_prefix, target_uri_prefix)
#         for v in matching_pairs_dict.values():
#             graph = remove_matched(graph, v, remove)
#         matching_pairs = mwgm(graph, source_uri_prefix)
#         if len(matching_pairs) > 0:
#             matching_pairs_dict[th] = matching_pairs
#         else:
#             return matching_pairs_dict
#     return matching_pairs_dict


def mwgm_level(sim_mat, threshold_list, source_class_uris, target_class_uris, references, remove='node',
               source_uri_prefix='s', target_uri_prefix='t'):
    print('threshold :', threshold_list)
    matching_pairs_dict = {}
    for th in threshold_list:
        graph = sim_graph(sim_mat, th, source_uri_prefix, target_uri_prefix)
        for v in matching_pairs_dict.values():
            graph = remove_matched(graph, v, remove)
        matching_pairs = mwgm(graph, source_uri_prefix)
        if len(matching_pairs) > 0:
            matching_pairs_dict[th] = matching_pairs
            level_eva(matching_pairs_dict, source_class_uris, target_class_uris, references)
        else:
            return matching_pairs_dict
    return matching_pairs_dict


def mwgm_multi(sim_mat, threshold, times, remove='node', source_uri_prefix='s', target_uri_prefix='t'):
    print('threshold : %f; times : %f' % (threshold, times))
    graph = sim_graph(sim_mat, threshold, source_uri_prefix, target_uri_prefix)
    matching_pairs_dict = {}
    for i in range(times):
        matching_pairs = mwgm(graph, source_uri_prefix)
        if len(matching_pairs) > 0:
            matching_pairs_dict[i] = matching_pairs
        else:
            return matching_pairs_dict
        graph = remove_matched(graph, matching_pairs, remove)
    return matching_pairs_dict


def remove_matched(graph, matching_pairs, remove='node'):
    if matching_pairs is None or len(matching_pairs) == 0:
        return graph
    # print("before removing, len is : %d" % graph.__len__())
    if remove == 'edge':
        for pair in matching_pairs:
            graph.remove_edge(pair[0], pair[1])
    else:
        for pair in matching_pairs:
            graph.remove_node(pair[0])
            graph.remove_node(pair[1])
    # print("after removing, len is : %d" % graph.__len__())
    return graph


def mwgm_once(sim_mat, threshold, source_uri_prefix='s', target_uri_prefix='t'):
    print('threshold : %f' % threshold)
    graph = sim_graph(sim_mat, threshold, source_uri_prefix, target_uri_prefix)
    return mwgm(graph, source_uri_prefix)


def mwgm(graph, source_uri_prefix='s'):
    edges = nx.max_weight_matching(graph, maxcardinality=False)
    matching_pairs = []
    keys = [k for k in edges.keys() if k.startswith(source_uri_prefix)]
    for key in keys:
        matching_pairs.append((key, edges[key]))
    return matching_pairs


def sim_graph(sim_mat, threshold, source_uri_prefix='s', target_uri_prefix='t'):
    row = sim_mat.shape[0]
    col = sim_mat.shape[1]
    graph = nx.Graph()
    for i, j in product(range(row), range(col)):
        if sim_mat[i, j] > threshold:
            graph.add_edge(str_splice(source_uri_prefix, i), str_splice(target_uri_prefix, j), weight=sim_mat[i, j])
    print("the len of graph is : %d " % graph.__len__())
    return graph


def evaluate(source_onto_uris, target_onto_uris, references, matchings, source_uri_prefix='s', target_uri_prefix='t'):
    reference_set = set()
    for reference in references:
        reference_set.add(str_splice(str_splice(source_uri_prefix, source_onto_uris.index(reference[0])),
                                     str_splice(target_uri_prefix, target_onto_uris.index(reference[1]))))
    matched_num = 0
    for matching in matchings:
        matching = str_splice(matching[0], matching[1])
        if matching in reference_set:
            matched_num += 1
    print("references : %f; matchings : %f; correct : %f" % (len(references), len(matchings), matched_num))
    recall = matched_num / len(references)
    precision = matched_num / len(matchings)
    f1 = 2 * precision * recall / (precision + recall)
    print("recall : %f" % recall)
    print("precision : %f" % precision)
    print("f1 : %f\n" % f1)


def level_eva(matching, source_class_uris, target_class_uris, references):
    matching_all = []
    for key in matching.keys():
        # print(len(matching[key]))
        matching_all.extend(matching[key])
    evaluate(source_class_uris, target_class_uris, references, matching_all)


def test(mat, min_threshold, source_onto_uris, target_onto_uris, references, source_uri_prefix='s',
         target_uri_prefix='t'):
    print('\nonce')
    threshold = min_threshold
    while threshold < 0.91:
        matchings = mwgm_once(mat, threshold, source_uri_prefix, target_uri_prefix)
        evaluate(source_onto_uris, target_onto_uris, references, matchings)
        threshold += 0.1

    print('\nlevel')
    threshold = 0.9
    threshold_list = []
    while threshold >= min_threshold:
        threshold_list.append(threshold)
        threshold -= 0.1
    mwgm_level(mat, threshold_list, source_onto_uris, target_onto_uris, references)


def str_splice(prefix, index):
    return prefix + "_" + str(index)
