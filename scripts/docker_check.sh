#!/bin/bash

###########################
#
#
#  Script to run the parser
#
#
###########################

TEMPLATE=$1

NOW=$(date +"%m_%d_%Y")

LOGFILE="${TEMPLATE}_docker_${NOW}.txt"

echo "cleaning files"
rm -rf *.txt

#run parse
python ../tools/dockerparse.py $TEMPLATE


# if no error, then build. 
if [ ! -e "error.txt" ]
  do 
    echo "Grabbing system version of Docker and kernel details"
    docker version > ${LOGFILE} && uname -a >> ${LOGFILE}

    docker build -t $TEMPLATE . >> ${LOGFILE}
  done
else
   print "Error file found. Aborting process."
