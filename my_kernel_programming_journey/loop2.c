#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int a;
    int num;
    system("clear");
    printf("Enter number: ");
    scanf("%d", &num);
    for(a = num; a>0; a=a-4)
    {
        printf("%d ",a);
    }
    printf("\n");
    return 0;
}