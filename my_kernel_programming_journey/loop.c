#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int i;
    int num;
    system("clear");
    printf("Enter your number: ");
    scanf("%d", &num);
    for(i = 1; i<=2*num-1; i=i+2)
    {
        printf("%d\n", i);
    }
}