#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/sysinfo.h>
#include <sys/utsname.h>
#include <sys/statvfs.h>

void get_uptime() {
FILE *fp = fopen("/proc/uptime", "r");
float uptime, idletime;
if (fp != NULL) {
    fscanf(fp, "%f %f", &uptime, &idletime);
    fclose(fp);
    int hours = (int)uptime / 3600;
    int minutes = ((int)uptime % 3600) / 60;
    int idle_hours = (int)idletime / 3600;
    int idle_minutes = ((int)idletime % 3600) / 60;

    printf("Uptime         : %d hours %d minutes\n", hours, minutes);
    printf("CPU Idle Time  : %d hours %d minutes\n", idle_hours, idle_minutes);
} 
    }

void get_memory_usage() {
    struct sysinfo info;
    sysinfo(&info);
    long total = info.totalram / (1024 * 1024);
    long free = info.freeram / (1024 * 1024);
    long used = total - free;
    printf("Memory Usage   : %ld MB used / %ld MB total\n", used, total);
}

void get_disk_usage(const char *path) {
    struct statvfs vfs;
    if (statvfs(path, &vfs) == 0) {
        unsigned long total = vfs.f_blocks * vfs.f_frsize;
        unsigned long free = vfs.f_bfree * vfs.f_frsize;
        unsigned long used = total - free;
        int percent = (int)((used / (float)total) * 100);
        printf("Disk Usage     : %d%% used of %s\n", percent, path);
    }
}

void get_cpu_usage() {
    FILE *fp = fopen("/proc/stat", "r");
    char buffer[1024];
    unsigned long user, nice, system, idle;
    if (fp != NULL) {
        fgets(buffer, sizeof(buffer), fp); // first line
        sscanf(buffer, "cpu  %lu %lu %lu %lu", &user, &nice, &system, &idle);
        fclose(fp);
        unsigned long total = user + nice + system + idle;
        int usage = (int)(((user + nice + system) / (float)total) * 100);
        printf("CPU Usage      : %d%%\n", usage);
    }
}

void get_logged_in_users() {
    FILE *fp = popen("who", "r");
    char line[256];
    int count = 0;
    printf("Users Logged In: ");
    while (fgets(line, sizeof(line), fp)) {
        char username[64];
        sscanf(line, "%s", username);
        if (count == 0)
            printf("%s", username);
        else
            printf(", %s", username);
        count++;
    }
    pclose(fp);
    printf(" (%d users)\n", count);
}

void get_running_processes() {
    FILE *fp = popen("ps -e --no-headers | wc -l", "r");
    int procs = 0;
    if (fp != NULL) {
        fscanf(fp, "%d", &procs);
        pclose(fp);
        printf("Running Procs  : %d\n", procs);
    }
}

int main() {
    struct utsname uname_data;
    uname(&uname_data);

    printf("===== System Information =====\n");
    printf("Hostname       : %s\n", uname_data.nodename);

    get_uptime();
    get_cpu_usage();
    get_memory_usage();
    get_disk_usage("/");
    get_logged_in_users();
    get_running_processes();

    printf("==============================\n");
    return 0;
}

