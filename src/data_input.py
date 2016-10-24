import rdflib as rl
import xml.dom.minidom as xml


def get_label(graph, class_uris):
    label_dict = []
    for uri in class_uris:
        label = [l for l in graph.objects(uri, rl.RDFS.label)]
        label_dict.append(label[0].value)
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
    return references


class DataSet:
    def __init__(self, source_owl_file, target_owl_file, reference_file):
        self.source_onto = rl.Graph()
        self.source_onto.load(source_owl_file)
        self.source_class_uris = [subject for subject in self.source_onto.subjects(rl.RDF.type, rl.OWL.Class) if
                                  'NCI' in subject]
        print('the number of classes in source ontology is %d' % len(self.source_class_uris))
        self.source_class_labels = get_label(self.source_onto, self.source_class_uris)
        print('the number of classes in source ontology that have labels is %d' % len(self.source_class_labels))

        self.target_onto = rl.Graph()
        self.target_onto.load(target_owl_file)
        self.target_class_uris = [subject for subject in self.target_onto.subjects(rl.RDF.type, rl.OWL.Class) if
                                  'MA' in subject]
        print('the number of classes in target ontology is %d' % len(self.target_class_uris))
        self.target_class_labels = get_label(self.target_onto, self.target_class_uris)
        print('the number of classes in target ontology that have labels is %d' % len(self.target_class_labels))

        self.references = reference_parser(reference_file)
        print('the number of references in source and target ontology is %d' % len(self.references))
