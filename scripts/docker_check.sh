#!/bin/bash

###########################
#
#
#  Script to run trhe parser
#
#
###########################

TEMPLATE=$1
LOGFILE="docker.txt"

echo "cleaning files"
rm -rf $LOGFILE

#run parse
python ../tools/dockerparse.py

echo "Grabbing system version of Docker and kernel details"
docker version > docker.txt && uname -a >> docker.txt

docker build -t $TEMPLATE . >> docker.txt
