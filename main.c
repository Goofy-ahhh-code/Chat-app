#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {

    int port = atoi(argv[1]);
    printf("Server will run on port %d\n", port);

    return 0;
}
