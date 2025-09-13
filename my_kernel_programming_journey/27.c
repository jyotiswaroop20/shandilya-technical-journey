#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int i;
    int j;
    for(i=0 , j=999; i<10; i++, j--)
    {
        printf("%d %d\n", i ,j);
    }
    system("sleep 7");
    system("clear");
    return 0;
}