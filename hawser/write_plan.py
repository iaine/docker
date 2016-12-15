'''
   Writing the plan for the Provenance
'''

import subprocess
import sys
import os

from rdflib import Namespace, URIRef, Graph, Literal
from rdflib.namespace import RDF, FOAF

#from docker-hawser import OS_Environment, Container_Environment

from operating_sys import OS_Environment

ose = OS_Environment()
g = Graph()

PROV = Namespace("http://www.w3.org/ns/prov#")
g.bind("prov", PROV)

DOCK = Namespace("http://www.containerprov.org/ns/docker#")
g.bind("docker", DOCK)

FRBR = Namespace("http://purl.org/vocab/frbr/core#")
g.bind("frbr", FRBR)

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
g.bind("rdfs", RDFS)

RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
g.bind("rdf", RDF)

OWL = Namespace("http://www.w3.org/2002/07/owl#")
g.bind("owl", OWL)

#set up FRBR Group 1 entities
g.add( (URIRef(DOCK.Name), RDFS.subClassOf , FRBR.Work) )
g.add( (URIRef(DOCK.Dockerfile), RDF.subClassOf , FRBR.Manifestation) )
g.add( (URIRef(DOCK.Container), RDF.subcClassOf , FRBR.Item) )

#set up FRBR group 2 entities
g.add( (URIRef(DOCK.Maintainer), RDF.subClassOf , FRBR.Person) )
g.add( (URIRef(DOCK.Organisation), RDF.subClassOf , FRBR.CorporateBody) )

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
container_temp = sys.argv[2]
container_version = sys.argv[3]
if template is None:
    print ("No file given")
    sys.exit(0)

g.add ( (RDF.type, RDF.about, URIRef(DOCK.Dockerfile)) )
#add the 'bibliographic' parts of the process
g.add( (URIRef(DOCK.Dockerfile), DOCK.Dockerfile , Literal(template) ) )
g.add( (URIRef(DOCK.Container), DOCK.Dockerfile , Literal(container_temp) ) )
g.add( (URIRef(DOCK.Dockerfile), DOCK.Dockerfile , Literal(str(container_temp) + ":" + str(container_version)) ) )
#now to add the activities

g.add ( (RDF.type, RDF.about, URIRef(DOCK.Dockerfile)) )
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
    g.add( (URIRef(DOCK.Container), DOCK.OSname, Literal(ose.get_os_name())) )
    g.add( (URIRef(DOCK.Container), DOCK.build, Literal(ose.get_os_build())) )
    g.add( (URIRef(DOCK.Container), DOCK.kernel, Literal(ose.get_os_kernel())) )
    g.add( (URIRef(DOCK.Container), DOCK.architecture, Literal(ose.get_os_arch())) )




g.serialize(destination=template + '_plan.ttl', format='turtle')
