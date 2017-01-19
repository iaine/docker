'''
   Writing the plan for the Provenance
'''

import subprocess
import sys
import os
import re

from datetime import datetime
from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import RDF, FOAF
from pytz import reference

from hawser import DockerHawser
from operating_sys import OS_Environment
from container import Container_Environment
from parse_kliko import parse_kliko

ose = OS_Environment()
ce = Container_Environment()
g = Graph()
pk = parse_kliko('kliko.yml')

#namespaces and binding
KLIKO = Namespace("http://www.example.org/ns/kliko#")
g.bind("kliko", KLIKO)

PROV = Namespace("http://www.w3.org/ns/prov#")
g.bind("prov", PROV)

DOCK = Namespace("http://www.example.org/ns/docker#")
g.bind("docker", DOCK)

FRBR = Namespace("http://purl.org/vocab/frbr/core#")
g.bind("frbr", FRBR)

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
g.bind("rdfs", RDFS)

RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
g.bind("rdf", RDF)

OWL = Namespace("http://www.w3.org/2002/07/owl#")
g.bind("owl", OWL)

TIME = Namespace("http://www.w3.org/2006/time#")
g.bind("time", TIME)

g.bind("foaf", FOAF)


template = sys.argv[1]
container_temp = sys.argv[2]
container_version = sys.argv[3]

if template is None:
    print ("No file given")
    sys.exit(0)


#set up FRBR Group 1 entities
g.add( (URIRef(DOCK.ContainerID), RDFS.subClassOf , FRBR.Work) )
g.add( (URIRef(DOCK.Dockerfile), RDFS.subClassOf , FRBR.Manifestation) )
g.add( (URIRef(DOCK.Container), RDFS.subClassOf , FRBR.Item) )

#set up FRBR group 2 entities
g.add( (URIRef(DOCK.Maintainer), RDFS.subClassOf , FRBR.Person) )
g.add( (URIRef(DOCK.Organisation), RDFS.subClassOf , FRBR.CorporateBody) )

#create orgnaisation
g.add( (DOCK.Organisation, RDF.about, Literal('Square Kilometre Array') ) )

#add the entities to the graph
g.add( (URIRef(DOCK.Hawser), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.Dockerfile), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.Container), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.Build), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.Tag), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.ErrorFile), RDF.type , PROV.Entity) )
g.add( (URIRef(DOCK.OS), RDF.type, PROV.Entity ) )
g.add( (URIRef(DOCK.Kernel), RDF.type, PROV.Entity ) )


# add activities
g.add( (URIRef(DOCK.Check), RDF.type , PROV.Activity) )
g.add( (URIRef(DOCK.Extraction), RDF.type , PROV.Activity) )
g.add( (URIRef(DOCK.Create), RDF.type , PROV.Activity) )
g.add( (URIRef(DOCK.Version), RDF.type , PROV.Activity) )

g.add ( (RDF.type, RDF.about, URIRef(DOCK.Dockerfile)) )
#add the 'bibliographic' parts of the process
g.add( (URIRef(DOCK.Dockerfile), DOCK.Dockerfile , Literal(template) ) )
g.add( (URIRef(DOCK.Container), DOCK.Container , Literal(container_temp) ) )
g.add( (URIRef(DOCK.ContainerID), DOCK.Dockerfile , Literal(str(container_temp) + ":" + str(container_version)) ) )
g.add( (URIRef(DOCK.ContainerID), PROV.wasGeneratedBy, URIRef(DOCK.Container)) )
#now to add the activities

g.add ( (RDF.type, RDF.about, URIRef(DOCK.Dockerfile)) )

# run the parser
DockerHawser(template).evaluate()
g.add( (URIRef(DOCK.Hawser), PROV.Check , URIRef(DOCK.Dockerfile )) )
g.add( (DOCK.ContainerID, RDF.resource , URIRef('http://www.example.org/dockerfile#' + str(template + "_docker.ttl"))) )

#set up the time
dtime = datetime.now()
localtz = reference.LocalTimezone()

g.add( (DOCK.createdAt, RDF.type, TIME.Instant) )
g.add( (DOCK.createdAt, TIME.timeZone, Literal(localtz.tzname(dtime)) ) )
g.add( (DOCK.createdAt, TIME.inXSDDateTime, Literal(dtime.isoformat()) ) )

#set up the maintainer
with open(template, 'r') as f:
    maintainer = re.search('(?<=MAINTAINER).*', f.read())
    maintain = str(maintainer.group(0)).strip().split()
    m = URIRef("http://example.org/people/" + str(maintain[0]))
    g.add ( (DOCK.Maintainer, RDF.about, m) )
    g.add( (m, RDF.type, FOAF.Person) )
    #g.add( (m, RDF.resource, DOCK.Maintainer ) )
    g.add( (m, DOCK.maintains, DOCK.Dockerfile ) )
    g.add( (m, FOAF.name, Literal(' '.join(maintain[0:-1])) ) )
    g.add( (m, FOAF.mbox, Literal(str(maintain[-1])) ) )
f.closed

g.add( (DOCK.Container, PROV.uses, DOCK.Organisation ) )

# write out the error
if os.path.isfile('error.txt'):
    g.add( (URIRef(DOCK.Command), PROV.Create , URIRef(DOCK.ErrorFile )) )
else:
   
    g.add( (URIRef(DOCK.OS), PROV.used, URIRef(DOCK.Extraction)) )
    g.add( (URIRef(DOCK.Kernel), PROV.used, URIRef(DOCK.Extraction)) )
    
    # build the container
    #p =  subprocess.check_output(['docker'," build -t " + container_temp + " ."])
    g.add( (DOCK.Build, PROV.used, DOCK.Command) )
    g.add( (DOCK.Build, PROV.used, DOCK.OS) )
    g.add( (DOCK.Build, PROV.used, DOCK.Dockerfile) )
    g.add( (DOCK.Container, PROV.wasGeneratedBy, DOCK.Dockerfile) )
    g.add( (DOCK.OS, DOCK.OSname, Literal(ose.get_os_name())) )
    g.add( (DOCK.OS, DOCK.build, Literal(ose.get_os_build())) )
    g.add( (DOCK.OS, DOCK.kernel, Literal(ose.get_os_kernel())) )
    g.add( (DOCK.OS, DOCK.architecture, Literal(ose.get_os_arch())) )
    g.add( (DOCK.Create, DOCK.dockerversion, Literal(ce.get_docker_version())) )

    host = "http://127.0.0.1:5000/" + str(container_temp) + ":" + str(container_version)
    #tag the container
    #p =  subprocess.check_output(['docker',"tag " + str(container_temp) + " " + host])
    g.add( (DOCK.Tag, PROV.used, DOCK.Command) )
    g.add( (DOCK.ContainerID, PROV.wasGeneratedBy, DOCK.Container) )


    g.add( (DOCK.Push, PROV.used, DOCK.Command) )
    #link to a Kliko file
    pk.parse_kliko_file()
    g.add( (KLIKO.file, RDF.resource, URIRef('http://www.example.org/kliko#' + str("kliko_kliko.xml")) ) )
    g.add( (KLIKO.file, PROV.used, DOCK.container))

g.serialize(destination=template + '_plan.xml', format='xml')
