FROM ubuntu:14.04

MAINTAINER Iain Emsley iain@example.org

RUN apt-get update

RUN apt-get install -y python-software-properties software-properties-common

RUN add-apt-repository ppa:radio-astro/main && \
add-apt-irepository multiverse

RUN apt-get update && \
    apt-get install -y oskar=2.6.1-1trusty && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
