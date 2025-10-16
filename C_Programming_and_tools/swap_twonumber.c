#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    system("clear");
    int a = 50;
    int b = 10;
    int c;
    printf("Number Before swapping: %d & %d\n",a,b);
    c = a;
    a = b;
    b = c;
    printf("Number Before swapping: %d & %d\n",a,b);
    return 0;
}