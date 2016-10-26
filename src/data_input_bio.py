import rdflib as rl
import xml.dom.minidom as xml


# 就取uri #之后的作为label
def get_label(graph, class_uris):
    label_dict = []
    for uri in class_uris:
        # print(uri.split('#')[1])
        label_dict.append(uri.split('#')[1])
    return label_dict


def reference_parser(file):
    references = []
    dom = xml.parse(file)
    maps = dom.getElementsByTagName('map')
    for map in maps:
        entity1 = map.getElementsByTagName('entity1')[0].getAttribute('rdf:resource')
        entity2 = map.getElementsByTagName('entity2')[0].getAttribute('rdf:resource')
        measure = map.getElementsByTagName('measure')[0].firstChild.data
        relation = map.getElementsByTagName('relation')[0].firstChild.data
        references.append((entity1, entity2, measure, relation))
    # print(references)
    return references


def list_2_str(no_str_list):
    return [str(l) for l in no_str_list]


class DataSet:
    """
    source_owl_file: 源本体文件
    """

    def __init__(self, source_owl_file, target_owl_file, source_key, target_key, reference_file):
        self.source_onto = rl.Graph()
        self.source_onto.load(source_owl_file)
        self.source_class_uris = [subject for subject in self.source_onto.subjects(rl.RDF.type, rl.OWL.Class) if
                                  source_key in subject]

        print('the number of classes in source ontology is %d' % len(self.source_class_uris))
        self.source_class_labels = get_label(self.source_onto, self.source_class_uris)
        print('the number of classes in source ontology that have labels is %d' % len(self.source_class_labels))
        self.source_class_uris = list_2_str(self.source_class_uris)
        # print(self.source_class_uris)

        self.target_onto = rl.Graph()
        self.target_onto.load(target_owl_file)
        self.target_class_uris = [subject for subject in self.target_onto.subjects(rl.RDF.type, rl.OWL.Class) if
                                  target_key in subject]

        print('the number of classes in target ontology is %d' % len(self.target_class_uris))
        self.target_class_labels = get_label(self.target_onto, self.target_class_uris)
        print('the number of classes in target ontology that have labels is %d' % len(self.target_class_labels))
        self.target_class_uris = list_2_str(self.target_class_uris)
        # print(self.target_class_uris)

        self.references = reference_parser(reference_file)
        print('the number of references in source and target ontology is %d' % len(self.references))
