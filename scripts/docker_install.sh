#!/bin/bash

############################
#
#  Script for the Docker installation tests
#
#  author: Iain Emsley <iain.emsley@kellogg.ox.ac.uk>
#
#  Use: docker_install.sh "user" "ip address"
#
############################

USER=$1
REMOTE=$2

#REPS=0

#while [ $REPS -lt 10 ]; do
time scp oskar.tar $USER@$REMOTE: 

ssh $USER@$REMOTE 'time docker load -i oskar.tar && docker run -d --privileged oskar'

echo "Teardown Remote Machine"
ssh $USER@$REMOTE 'rm -rf oskar.tar && docker rm $(docker ps -a -q) && docker rmi $(docker images -q)'

   let REPS=REPS+1
#done
