from itertools import product
import numpy as np
import Levenshtein as lev


def label_sim_matrix(source_labels, target_labels):
    s_len = len(source_labels)
    t_len = len(target_labels)
    mat = np.zeros([s_len, t_len])
    for i, j in product(range(s_len), range(t_len)):
        dist = edit_distance(source_labels[i].lower(), target_labels[j].lower())
        if dist > 0:
            mat[i, j] = dist
    return mat


def edit_distance(str1, str2):
    dist = lev.distance(str1, str2)
    min_len = min(len(str1), len(str2))
    return round(1 - dist / min_len, 4)
