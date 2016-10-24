from data_input import *
from similarity import *
from mwgm import *
import os

anatomy_folder = '../data/anatomy'
human_owl_file = os.path.join(anatomy_folder, 'human.owl')
mouse_owl_file = os.path.join(anatomy_folder, 'mouse.owl')
human_mouse_reference = os.path.join(anatomy_folder, 'reference.rdf')

dataset = DataSet(human_owl_file, mouse_owl_file, human_mouse_reference)
sim_mat = label_sim_matrix(dataset.source_class_labels, dataset.target_class_labels)
graph = sim_graph(sim_mat)
edges = mwgm(graph)
print(len(edges), edges)
