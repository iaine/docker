#Examples

This is contains a Dockerfile originally created for the OSKAR simulator
and an example Kliko file.

The Dockerfile_plan.ttl is a Turtle format of the provenance output for the 
build of the Dokcerfile into a container

The Dockerfile_docker.ttl is a Turtle file of the Operating System, maintainer
and software packages. 

The kliko.yml_kliko.ttl is a Turtle format of the result of parsing the Kliko
workflow file. 

The parameters to generate these are:

    python ../../hawser/write_plan.py Dockerfile temp 0.1 kliko.yml


