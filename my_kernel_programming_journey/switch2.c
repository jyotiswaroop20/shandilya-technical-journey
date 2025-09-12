#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    char choice;
    char extra;
    system("clear");
    printf("This is simple program\n");
    printf("Enter your Choice[from a to c]: ");
    if(scanf("%c%c", &choice , &extra)!=2 || extra != '\n' || choice < 'a' || choice > 'z')
    {
        printf("Invalid Value! Enter only a single small letter [from a to c].\n");
        system("sleep 5");
        system("clear");
        return 1;   
    }
    else
    {
        switch (choice) {
        
        case 'a':
            printf("It's 'a'!\n");
            system("sleep 7");
            system("clear");
            break;
        
        case 'b':
            printf("It's 'b'!\n");
            system("sleep 7");
            system("clear");
            break;

        case 'c':
            printf("It's 'c'!\n");
            system("sleep 7");
            system("clear");
            break;

        default:
            printf("Invalid Choice!\n");
            break;
        }
    }
    return 0;
}