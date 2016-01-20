FROM ubuntu-14.04

RUN /usr/bin/wget http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb && \
/usr/bin/dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb && \
/usr/bin/wget http://www.oerc.ox.ac.uk/~ska/oskar/OSKAR-Source.zip && \
/usr/bin/tar -xzf OSKAR-Source.zip && \
 apt-get update && \
apt-get install cmake \
cuda \
g++ \
libqt4-dev \
liblapack-dev && \
cd OSKAR-Source && \
mkdir build && \
cd build && \
cmake ../ && \
make && \
sudo make install


