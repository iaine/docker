#!/bin/bash

rm -f Dockerfile

cat os.docker >> Dockerfile
cat repo.docker >> Dockerfile
cat oskar.docker >> Dockerfile
