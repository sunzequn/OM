from data_input_bio import *
from similarity import *
from match import *
import os

bio_folder = '../data/LargeBio_dataset_oaei2016'
fma2nci_small_owl_file = os.path.join(bio_folder, 'oaei_FMA_small_overlapping_nci.owl')
nci2fma_small_owl_file = os.path.join(bio_folder, 'oaei_NCI_small_overlapping_fma.owl')
fma2nci_small_reference = os.path.join(bio_folder, 'oaei_FMA2NCI_UMLS_mappings_with_flagged_repairs.rdf')

dataset = DataSet(fma2nci_small_owl_file, nci2fma_small_owl_file, 'fma', 'nci', fma2nci_small_reference)
sim_mat = label_sim_matrix(dataset.source_class_labels, dataset.target_class_labels, edit_distance)

print("\nsim ------")
test(sim_mat, 0.5, dataset.source_class_uris, dataset.target_class_uris, dataset.references)

print("\n mcd ---- ")
mcd = mcd_matrix(sim_mat)
test(mcd, 0.3, dataset.source_class_uris, dataset.target_class_uris, dataset.references)

print("\n mcd posi ---- ")
mcd_posi = mcd_posi_matrix(sim_mat)
test(mcd_posi, 0.5, dataset.source_class_uris, dataset.target_class_uris, dataset.references)
