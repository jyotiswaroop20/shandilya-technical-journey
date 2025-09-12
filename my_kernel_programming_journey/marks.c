#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    float n;
    char extra;
    system("clear");
    printf("This program is for deciding grade\n");
    printf("Enter your percentage: ");
    if(scanf("%f%c", &n , &extra)!=2 || extra != '\n')
    {
        printf("Invalid Value! Enter Integer or Decimal only \n");
        system("sleep 5");
        system("clear");
        return 1;   
    }
    else
    {
        if (n>=90 && n<=100)
        {
            printf("A Grade\n");
            system("sleep 5");
            system("clear");       
        }
        else if (n>=80 && n<=89.99)
        {
            printf("B Grade\n");
            system("sleep 5");
            system("clear");
        }
        else if (n>=70 && n<=79.99)
        {
            printf("C Grade\n");
            system("sleep 5");
            system("clear"); 
        }
        else if (n>100)
        {
            printf("Invalid Percentage! Value should not be more than 100\n");
            system("sleep 5");
            system("clear"); 
        }
        
        else
        {
            printf("Fail\n");
            system("sleep 5");
            system("clear"); 
        }
    }
    return 0;
}