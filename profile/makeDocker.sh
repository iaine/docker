#!/bin/bash

rm -f Dockerfile

cat dock/os.docker >> Dockerfile
cat dock/repo.docker >> Dockerfile
cat dock/oskar.docker >> Dockerfile
