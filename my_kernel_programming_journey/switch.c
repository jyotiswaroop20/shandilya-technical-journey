#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int choice;
    char extra;
    system("clear");
    printf("This program is for display system information\n");
    printf("Enter your Choice[from 0 to 6]: ");
    if(scanf("%d%c", &choice , &extra)!=2 || extra != '\n')
    {
        printf("Invalid Value! Enter Integer only \n");
        system("sleep 5");
        system("clear");
        return 1;   
    }
    else
    {
        switch (choice)
        {
        case 0:
            printf("This Zero Choice shows full system and kernel details.\n");
            system("uname -a");
            system("sleep 7");
            system("clear");
            break;
        case 1:
            printf("This First Choice shows the systems memory usage in MB (megabytes).\n");
            system("free -m");
            system("sleep 7");
            system("clear");
            break;
        case 2:
            printf("This Second Choice shows the kernel version of your system.\n");
            system("uname -r");
            system("sleep 7");
            system("clear");
            break;
        case 3:
            printf("This Third Choice shows real-time processes and resource usage.\n");
            system("top");
            system("sleep 7");
            system("clear");
            break;
        case 4:
            printf("This Fourth Choice shows a calendar of the current month.\n");
            system("cal");
            system("sleep 7");
            system("clear");
            break;
        case 5:
            printf("This Fifth Choice shows the current system date and time of the system.\n");
            system("date");
            system("sleep 7");
            system("clear");
            break;
        case 6:
            printf("This Sixth Choice installs, starts, and enables the Apache (httpd) web server.\n");
            system("dnf install httpd -y");
            system("systemctl start httpd");
            system("systemctl enable --now httpd");
            system("sleep 7");
            system("clear");
            break;
        
        default:
            printf("Invalid Choice\n");
            break;
        }
    }
    return 0;
}