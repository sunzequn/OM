from itertools import product
import numpy as np
import Levenshtein as lev


# "From Diversity-based Prediction to Better Ontology & Schema Matching." WWW2016
def mcd_matrix(sim_matrix):
    n, m = sim_matrix.shape[0], sim_matrix.shape[1]
    row_sum = np.sum(sim_matrix, axis=1)
    col_sum = np.sum(sim_matrix, axis=0)
    # print(type(row_sum), row_sum.shape)
    # print(type(col_sum), col_sum.shape)
    mcd = np.zeros((n, m))
    for i, j in product(range(n), range(m)):
        mu = (row_sum[i,] + col_sum[j,] - sim_matrix[i, j]) / (n + m - 1)
        delte = np.square(sim_matrix[i, j] - mu)
        mcd[i, j] = delte
    return mcd


def mcd_posi2_matrix(sim_matrix):
    n, m = sim_matrix.shape[0], sim_matrix.shape[1]
    row_sum = np.sum(sim_matrix, axis=1)
    col_sum = np.sum(sim_matrix, axis=0)
    # print(type(row_sum), row_sum.shape)
    # print(type(col_sum), col_sum.shape)
    mcd = np.zeros((n, m))
    for i, j in product(range(n), range(m)):
        mu = (row_sum[i,] + col_sum[j,] - sim_matrix[i, j]) / (n + m - 1)
        delte = max(0, (sim_matrix[i, j] - mu) / sim_matrix[i, j])
        mcd[i, j] = delte
    return mcd


def mcd_posi_matrix(sim_matrix):
    n, m = sim_matrix.shape[0], sim_matrix.shape[1]
    row_sum = np.sum(sim_matrix, axis=1)
    col_sum = np.sum(sim_matrix, axis=0)
    # print(type(row_sum), row_sum.shape)
    # print(type(col_sum), col_sum.shape)
    mcd = np.zeros((n, m))
    for i, j in product(range(n), range(m)):
        mu = (row_sum[i,] + col_sum[j,] - sim_matrix[i, j]) / (n + m - 1)
        # 这个地方取平方是没有意义的，和mcd结果一样。值得思考。
        delte = max(0, sim_matrix[i, j] - mu)

        mcd[i, j] = delte
    return mcd


# 太费了,数值太小
def prob_matrix(sim_matrix):
    n, m = sim_matrix.shape[0], sim_matrix.shape[1]
    for i, j in product(range(n), range(m)):
        if sim_matrix[i, j] < 0.4:
            sim_matrix[i, j] = 0
    row_sum = np.sum(sim_matrix, axis=1)
    col_sum = np.sum(sim_matrix, axis=0)
    # print(type(row_sum), row_sum.shape)
    # print(type(col_sum), col_sum.shape)
    mat = np.zeros((n, m))
    for i, j in product(range(n), range(m)):
        if row_sum[i,] > 0 and col_sum[j,] > 0:
            mat[i, j] = np.log2(1 + (sim_matrix[i, j] / row_sum[i,]) * (sim_matrix[i, j] / col_sum[j,]))
    return mat


def label_sim_matrix(source_labels, target_labels, sim_func):
    s_len = len(source_labels)
    t_len = len(target_labels)
    mat = np.zeros([s_len, t_len])
    for i, j in product(range(s_len), range(t_len)):
        dist = sim_func(source_labels[i].lower(), target_labels[j].lower())
        if dist > 0:
            mat[i, j] = dist
    # print(mat)
    return mat


def edit_distance(str1, str2):
    dist = lev.distance(str1, str2)
    min_len = min(len(str1), len(str2))
    return round(1 - dist / min_len, 4)

#
# a = np.matrix('1 2 7; 3 4 8; 5 6 9; 1 3 6')
# print(a)
# mcd_matrix(a)
