#include <stdio.h>
#include <stdlib.h>
int i = 1;

int main(void)
{
    system("clear");
    while(i<=20){
        
        printf("i is now %d\n", i*2);
        i++; 
    }
    printf("All done!\n");
return 0;
}