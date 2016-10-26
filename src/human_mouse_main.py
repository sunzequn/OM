from data_input import *
from similarity import *
from match import *
import os

anatomy_folder = '../data/anatomy'
human_owl_file = os.path.join(anatomy_folder, 'human.owl')
mouse_owl_file = os.path.join(anatomy_folder, 'mouse.owl')
human_mouse_reference = os.path.join(anatomy_folder, 'reference.rdf')

dataset = DataSet(mouse_owl_file, human_owl_file, 'MA', 'NCI', human_mouse_reference)
sim_mat = label_sim_matrix(dataset.source_class_labels, dataset.target_class_labels, edit_distance)

# pairwise
# matching = pairwise(sim_mat, 0.1)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.2)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.3)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.4)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.5)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.6)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.7)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.8)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = pairwise(sim_mat, 0.9)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.referenc=es, matching)

# print("------")
# sim_mat = prob_matrix(sim_mat)

# matching = mwgm_once(sim_mat, 0.4)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.5)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.6)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.7)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.8)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.9)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)

# print("------")

# 这个方法在求1:1的匹配上面是失败的
# matching = mwgm_multi(sim_mat, 0.4, 2, remove='node')
# print(len(matching))
# matching_all = []
# for i in range(len(matching)):
#     print(len(matching[i]))
#     matching_all.extend(matching[i])
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching_all)

# print("------")



# 这个方法在求1:1的匹配上面是有一定效果的的
# matching = mwgm_level(sim_mat, 0.9, 0.8, 0.7, 0.6, 0.5)
# matching_all = []
# for key in matching.keys():
#     print(len(matching[key]))
#     matching_all.extend(matching[key])
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching_all)

# print("------")


# matching = mwgm_once(sim_mat, 0.3)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.4)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.5)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.6)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.7)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.8)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
# matching = mwgm_once(sim_mat, 0.9)
# test(dataset.source_class_uris, dataset.target_class_uris, dataset.references, matching)
