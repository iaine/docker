'''
   The browser code
'''

import rdflib


class Browser():

    def __init__(self):
        '''
          Set up the graph
        '''
        self.g = rdflib.Graph()
        #self.uri['http://www.example.org/ns/ska#'] = "ska"

    def parse_file (self, filename):
        '''
           Open the file
        '''
        self.g.parse("../hawser/" + filename)

    
    def open_query(self, sparql_file):
        '''
            Open the Sparql query file
        '''
        if sparql_file is None:
            print ("No sparql file given")

        with open(sparql_file, 'rb') as f:
            return f.read()

    def browse(self, rdf_file, sparql):
        '''
          Public function to browse the file
        '''
        self.parse_file(rdf_file)
        
        query_res = self.g.query(self.open_query(sparql))

        return [(row['s'].toPython(), row['p'].toPython(),row['o'].toPython()) for row in query_res]

    def clean_ns(self, d):
        '''

         '''
        pass
