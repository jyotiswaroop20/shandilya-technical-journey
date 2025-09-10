#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    system("clear");
    int age1,age2,age3;
    printf("Enter 1st age : ");
    scanf("%d", &age1);

    printf("Enter 2nd age : ");
    scanf("%d", &age2);

    printf("Enter 3rd age : ");
    scanf("%d", &age3);
    if(age1 == age2 || age2 ==  age3 || age3 == age1 || age1 == age2 == age3)
    {
        printf("Numbers should not be same\n");
    }
    else
    {
        if(age1 >= age2 && age1 >= age3){
            printf("%d is big\n", age1);
        }
        else if(age2 > age1 && age2 > age3)
        {
            printf("%d is big\n",age2);
        }
        else if(age3 > age1 && age3 > age2)
        {
            printf("%d is big\n", age3);
        }
    }
return 0; 
}