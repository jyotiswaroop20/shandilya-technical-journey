#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pwd.h>

int main() {
    FILE *fp;
    char *username;
    struct passwd *pw;

    // Get current user ID
    uid_t uid = getuid();

    // Get user info using UID
    pw = getpwuid(uid);
    if (pw == NULL) {
        perror("getpwuid failed");
        return 1;
    }

    username = pw->pw_name;

    // Open log file in append mode
    fp = fopen("user_welcome.log", "a");
    if (fp == NULL) {
        perror("Unable to open log file");
        return 1;
    }

    // Write welcome message
    fprintf(fp, "Welcome %s!\n", username);

    fclose(fp);
    return 0;
}

