'''
   Parse the Kliko file
'''
import yaml
from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import RDF, FOAF

#namespaces and binding
KLIKO = Namespace("http://www.example.org/ns/kliko#")
g.bind("docker", KLIKO)

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
g.bind("rdfs", RDFS)

RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
g.bind("rdf", RDF)

OWL = Namespace("http://www.w3.org/2002/07/owl#")
g.bind("owl", OWL)

TIME = Namespace("http://www.w3.org/2006/time#")
g.bind("time", TIME)

g.bind("foaf", FOAF)

class parse_kliko():

    def __init__(self, fname):
        self.kliko = fname
        self.g = Graph()

    def parse_kliko_file(self):
        data = None
        with open(self.fname, 'r') as f:
            d = f.read()

        data = yaml.load(d)

        self.g.add( (URIRef(KLIKO.file), KLIKO.file , Literal(fname) ) )
        self.g.add( (URIRef(KLIKO.file), RDFS.description , Literal("Description of Kliko file") ) )
        self.g.add( (URIRef(KLIKO.file), KLIKO.name , Literal(data['name']) ) )
        self.g.add( (URIRef(KLIKO.file), KLIKO.io , Literal(data['io']) ) )       
        self.g.add( (URIRef(KLIKO.file), KLIKO.schema , Literal(data['schema_version']) ) )
        self.g.add( (URIRef(KLIKO.file), RDFS.description , Literal(data['description']) ) )
        self.g.add( (URIRef(KLIKO.file), KLIKO.schema , URIRef(data['url']) ) )
        #get the sections
        for sections in data['sections']:
            self.g.add( (URIRef(KLIKO.parameters), KLIKO.parameters , Literal(section['parameters']) ) )
            self.g.add( (URIRef(KLIKO.parameters), RDF.description , Literal(section['description']) ) )
            #get the fields
            for field in section['fields']:
                self.g.add( (URIRef(KLIKO.parameters), KLIKO.field , Literal(field['name']) ) )
                self.g.add( (URIRef(KLIKO.parameters), KLIKO.field , Literal(field['initial']) ) )
                self.g.add( (URIRef(KLIKO.parameters), KLIKO.field , Literal(field['type']) ) )
        g.serialize(destination=template + '_kliko.xml', format='xml')
