'''
   Parse the Kliko file
'''
import yaml
from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import RDF

KLIKO = Namespace("http://www.example.org/ns/kliko#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

class parse_kliko():

    def __init__(self, fname):
        self.kliko = fname
        self.g = Graph()
        self.g.bind("kliko", KLIKO)
        self.g.bind("rdfs", RDFS)
        self.g.bind("rdf", RDF)

    def parse_kliko_file(self):
        data = None
        with open(self.kliko, 'r') as f:
            d = f.read()

        data = yaml.load(d)

        self.g.add( (URIRef(self.kliko), RDFS.type, KLIKO.file ) )
        self.g.add( (KLIKO.file, KLIKO.name , Literal(data['name']) ) )
        self.g.add( (KLIKO.file, KLIKO.io , Literal(data['io']) ) )       
        self.g.add( (KLIKO.file, KLIKO.schema , Literal(data['schema_version']) ) )
        self.g.add( (KLIKO.file, RDFS.description , Literal(data['description']) ) )
        self.g.add( (KLIKO.file, KLIKO.schema , URIRef(data['url']) ) )
        self.g.add( (KLIKO.section, KLIKO.file , KLIKO.file ) )
        self.g.add( (KLIKO.parameter, KLIKO.file , KLIKO.section) )

        #get the sections
        for section in data['sections']:
            self.g.add( (URIRef(section['name']), RDF.type , KLIKO.section ) )
            self.g.add( (KLIKO.section, RDFS.description , Literal(section['description']) ) )
            #get the fields
            for field in section['fields']:
                self.g.add( (URIRef(field['name']), RDF.type , KLIKO.parameter ) )
                self.g.add( (URIRef(field['name']), KLIKO.parameter , Literal(field['name']) ) )
                self.g.add( (URIRef(field['name']), KLIKO.parameter , Literal(field['initial']) ) )
                self.g.add( (URIRef(field['name']), KLIKO.parameter , Literal(field['type']) ) )
        self.g.serialize(destination=self.kliko + '_kliko.ttl', format='ttl')
