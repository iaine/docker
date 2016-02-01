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

  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, cid, "/blkio.io_serviced");
  fileRead(buf);

  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, cid, "/blkio.io_queued");
  fileRead(buf);

  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, cid, "/blkio.io_service_bytes");
  fileRead(buf);

  snprintf(buf, sizeof buf, "%s%s%s", blkioFile, cid, "/blkio.io_sectors");
  fileRead(buf);

  return EXIT_SUCCESS;  
}
