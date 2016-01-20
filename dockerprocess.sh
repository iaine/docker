#!/bin/bash

DOCKERNAME=$1

#docker run -ti ${DOCKERNAME}

PID=`docker ps -q | xargs docker inspect --format '{{.State.Pid}}, {{.ID}}' | cut -d ',' -f1`

echo ${PID}

#or pgrep docker
