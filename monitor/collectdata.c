#include <fcntl.h>
#include <sched.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define errExit(msg)    do { perror(msg); exit(EXIT_FAILURE); \
                           } while (0)


/* Read the file and send the contents */
void
fileRead(char* buf) {

  FILE *fd;
  char *buff = buf;

  //snprintf(buf, 100, "%s%s%s", fname, cid, "/memory.stat");

  char contents[100];
  fd = fopen(buff, "rb");
    if (!fd) {
      errExit("open");   
  }

  while (fgets(contents, 300, (FILE*)fd) != NULL ) {
      printf(". %s\n", contents );
  }

  fclose(fd);

  buf[0] = 0;
}

int
main(int argc, char *argv[])
{
  char memFile[50] = "/sys/fs/cgroup/memory/docker/";
  char cpuFile[50] = "/sys/fs/cgroup/cpuacct/docker/";
  char blkioFile[50] = "/sys/fs/cgroup/blkio/docker/";
  
  if (argc < 2) {
    fprintf(stderr, "usage %s <long containerid> \n", argv[0]);
    exit(EXIT_FAILURE);
  }

  char *cid = argv[1];
  char buf[150];
  snprintf(buf, sizeof buf, "%s%s%s", memFile, cid, "/memory.stat");
  fileRead(buf);

  snprintf(buf, sizeof buf, "%s%s%s", cpuFile, cid, "/cpuacct.stat");
  fileRead(buf);

  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, argv[1], "/blkio.io_serviced");
  fileRead(buf);

/*
  fd = fopen(buf, "rb");
  if (!fd) {
    errExit("open");
  }
  char contents1[2048];

  while (fgets(contents1, 300, (FILE*)fd) != NULL ) {
    printf("cpu %s\n", contents1 );
  }

  fclose(fd);

  char contents2[1024];
  buf[0] = 0;
  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, argv[1], "/blkio.io_serviced");

  
  fd = fopen(buf, "rb");
  if (!fd) {
    errExit("open");
  }

  while (fgets(contents2, 300, (FILE*)fd) != NULL ) {
    printf("blkio %s\n", contents2 );
  }

  fclose(fd);

  char contents3[1024];
  buf[0] = 0;
  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, argv[1], "/blkio.io_queued");

  
  fd = fopen(buf, "rb");
  if (!fd) {
    errExit("open");
  }

  while (fgets(contents3, 300, (FILE*)fd) != NULL ) {
    printf("blkio %s\n", contents3 );
  }

  fclose(fd);

  char contents4[1024];
  buf[0] = 0;
  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, argv[1], "/blkio.io_service_bytes");

  fd = fopen(buf, "rb");
  if (!fd) {
    errExit("open");
  }

  while (fgets(contents4, 300, (FILE*)fd) != NULL ) {
    printf("blkio %s\n", contents4 );
  }

  char contents5[1024];
  buf[0] = 0;
  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, argv[1], "/blkio.sectors");

  fd = fopen(buf, "rb");
  if (!fd) {
    errExit("open");
  }

  while (fgets(contents5, 300, (FILE*)fd) != NULL ) {
    printf("blkio %s\n", contents5 );
  }


  fclose(fd);*/
  //int i;
  //for (i = 0; i < sizeof iostat; i++) {
    //printf("gggg %d\n", iostat[i] );
 // }
 

  return EXIT_SUCCESS;  
}
