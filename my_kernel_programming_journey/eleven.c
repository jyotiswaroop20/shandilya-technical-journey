#include <stdio.h>
#include <stdlib.h>

int main() {
    char choice;

    printf("Choose an option:\n");
    printf("d = Show Date\n");
    printf("l = List Files\n");
    printf("u = Show Uptime\n");
    printf("Enter your choice: ");
    scanf(" %c", &choice);

    if (choice == 'd') {
        system("date");
    } 
    else if (choice == 'l') {
        system("ls -l");
    } 
    else if (choice == 'u') {
        system("uptime");
    } 
    else {
        printf("Invalid choice!\n");
    }

    return 0;
}

