#!/bin/bash

PROCNAME=$1

NCID=$(docker run -d ${PROCNAME})

TASKS=/sys/fs/cgroup/devices/docker/$NCID*/tasks

PID=$(head -n 1 $TASKS)

echo $PID
