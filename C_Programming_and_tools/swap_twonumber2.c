#include <stdlib.h>
#include <stdio.h>
int main(void)
{
    system("clear");
    int a = 50;
    int b = 10;
    printf("Number Before swapping: %d & %d\n",a,b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("Number Before swapping: %d & %d\n",a,b);
    return 0;
}