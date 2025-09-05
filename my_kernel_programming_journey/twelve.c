#include <stdio.h>
#include <stdlib.h>

int main() {
    char choice;

    do {
        printf("\n===== Mini System Program =====\n");
        printf("d = Show Date & Time\n");
        printf("l = List Files\n");
        printf("u = Show Uptime\n");
        printf("m = Show Memory Usage\n");
	printf("b = Show Block Devices\n");
        printf("q = Quit\n");
        printf("Enter your choice: ");
        scanf(" %c", &choice);

        switch (choice) {
            case 'd':
                system("date");
                break;
            case 'l':
                system("ls -l");
                break;
            case 'u':
                system("uptime");
                break;
            case 'm':
                system("free -h");
                break;
	    case 'b':
                system("lsblk");
                break;
            case 'q':
                printf("Exiting program... Bye!\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }

    } while (choice != 'q');

    return 0;
}

