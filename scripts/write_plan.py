'''
   Writing the plan for the Provenance
'''

import subprocess
import sys
import os

from rdflib import Namespace, URIRef, Graph
from rdflib.namespace import RDF, FOAF

#from docker-hawser import OS_Environment, Container_Environment

g = Graph()

PROV = Namespace("http://www.w3.org/ns/prov#")
g.bind("prov", PROV)

DOCK = Namespace("http://www.example.org/ns/ska#")
g.bind("docker", DOCK)

FRBR = Namespace("http://purl.org/vocab/frbr/core#")
g.bind("frbr", FRBR)

#add the entities to the graph
g.add( (URIRef(DOCK.Hawser), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.Dockerfile), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.Container), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.Command), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.ErrorFile), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.OS), RDF.type, PROV.Entity ) )
g.add( (URIRef(DOCK.Kernel), RDF.type, PROV.Entity ) )


# add activities
g.add( (URIRef(DOCK.Check), RDF.type , PROV.Activity) )
g.add( (URIRef(DOCK.Extraction), RDF.type , PROV.Activity) )
g.add( (URIRef(DOCK.Create), RDF.type , PROV.Activity) )
g.add( (URIRef(DOCK.Version), RDF.type , PROV.Activity) )

template = sys.argv[1]
if template is None:
    sys.exit()

#now to add the activities

# run the parser
#p = subprocess('python', "../tools/dockerparse.py template")
g.add( (URIRef(DOCK.Hawser), PROV.Check , URIRef(DOCK.Dockerfile )) )

# write out the error
if os.path.isfile('error.txt'):
    g.add( (URIRef(DOCK.Command), PROV.Create , URIRef(DOCK.ErrorFile )) )
else:

    # extract OS details
    #p = subprocess('python', "../tools/dockerparse.py template")
    
    g.add( (URIRef(DOCK.OS), PROV.used, URIRef(DOCK.Extraction)) )
    # extract Ubuntu details
    #p = subprocess('python', "-a")
    g.add( (URIRef(DOCK.Kernel), PROV.used, URIRef(DOCK.Extraction)) )
    # build the container
    #p =  subprocess('docker' "build -t template . >> ${LOGFILE}")
    g.add( (URIRef(DOCK.Create), PROV.used, URIRef(DOCK.Command)) )
    g.add( (URIRef(DOCK.Container), PROV.wasGeneratedBy, URIRef(DOCK.Dockerfile)) )

g.serialize(destination=template + '_plan.ttl', format='turtle')
