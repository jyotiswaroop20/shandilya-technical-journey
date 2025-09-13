#include <stdio.h>
int plus_one(int x , int y)
{
    return x + y;
}
int main(void)
{
    int i = 17, j = 12;
    int k;
    k = plus_one(i,j);
    printf("Sum of two numbers is %d\n", k);
}