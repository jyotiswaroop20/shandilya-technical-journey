// welcome_logout_msg.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char *username = getenv("USER");
    time_t now;
    time(&now);
    struct tm *local = localtime(&now);

    if (argc > 1 && strcmp(argv[1], "logout") == 0) {
        printf("Goodbye %s! You logged out at: %02d-%02d-%04d %02d:%02d:%02d\n",
            username,
            local->tm_mday, local->tm_mon + 1, local->tm_year + 1900,
            local->tm_hour, local->tm_min, local->tm_sec);
        sleep(2);
        system("clear");
    } else {
        printf("Welcome %s! You logged in at: %02d-%02d-%04d %02d:%02d:%02d\n",
            username,
            local->tm_mday, local->tm_mon + 1, local->tm_year + 1900,
            local->tm_hour, local->tm_min, local->tm_sec);
    }

    return 0;
}

