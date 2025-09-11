#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int i=1;
    int num;
    char extra;
    system("clear");
    printf("Enter your number to print desired table: ");
    if(scanf("%d%c",&num,&extra) != 2 || extra != '\n')
    {
        printf("Invalid input!\n");
        return 1;
    }
    else{
        do
        {
            printf("%d\n", i*num);
            i++;
        } while (i<=10);
        system("sleep 6");
        system("clear");
    }
    return 0;
}