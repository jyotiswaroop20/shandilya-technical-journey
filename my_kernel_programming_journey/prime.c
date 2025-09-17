#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int n;
    int a = 0;
    char extra;
    system("clear");
    printf("Enter the number: ");
    if(scanf("%d%c", &n,&extra) != 2 || extra != '\n')
    {
        printf("Invalid Value! Enter Integer only \n");
        system("sleep 5");
        system("clear");
        return 1;
    }
    else{
            for(int i = 2; i<n-1; i++)
            {
                if (n%i == 0)
                {
                    a = 1;
                    break;
                }
            }
        }
        if (n==1 && n==2)
        {
            printf("This number is neither prime nor composite\n");
        }
        else if(a == 0)
        {
            printf("The gien number is prime\n");
        }
        else
        {
            printf("The given number is composite\n");
        }
    return 0;
}