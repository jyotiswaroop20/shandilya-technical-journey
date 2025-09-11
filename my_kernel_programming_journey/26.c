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
    else
    {
        for(i=i; i<=10; i++)
        printf("%d\n", i*num);
    }
        system("sleep 7");
        system("clear");
    return 0;
}