FROM ubuntu-14.04

RUN apt-get update && \
apt-get install build-essential && \
cmake &&\ 
gfortran &&\
g++ &&\
libncurses5-dev &&\
libreadline-dev &&\
flex &&\
bison &&\
libblas-dev && \
liblapacke-dev && \
libcfitsio3-dev &&\
wcslib-dev && \
git && \
git clone https://github.com/casacore/casacore && \
cd casacore && \
mkdir build && \
cd build && \
cmake && \
make && \
make install
