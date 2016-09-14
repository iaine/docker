#!/bin/bash

################
#
#  Script to run a docker image and retrieve its PID
#
#  author: Iain Emsley
#
################

PROCNAME=$1

NCID=$(docker run -d ${PROCNAME})

TASKS=/sys/fs/cgroup/devices/docker/$NCID/tasks

PID=$(head -n 1 $TASKS)

echo $PID
