#!/bin/bash

###########################
#
#
#  Script to run trhe parser
#
#
###########################

TEMPLATE=$1

NOW=$(date +"%m_%d_%Y")

LOGFILE="${TEMPLATE}_docker_${NOW}.txt"

echo "cleaning files"
rm -rf *.txt

#run parse
python ../tools/dockerparse.py

echo "Grabbing system version of Docker and kernel details"
docker version > ${LOGFILE} && uname -a >> ${LOGFILE}

docker build -t $TEMPLATE . >> ${LOGFILE}
