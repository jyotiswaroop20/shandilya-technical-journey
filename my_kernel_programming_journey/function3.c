#include <stdio.h>
int increment(int a)
{
    a++;
    return a;
}
int main(void)
{
    int i = 10;
    int j;
    j = increment(i);
    printf("i = %d\n", j);
    return 0;
}