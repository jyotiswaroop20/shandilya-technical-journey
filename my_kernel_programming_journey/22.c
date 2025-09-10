#include <stdio.h>
int main(void)
{
    int a,b,c;
    printf("Enter 1st side : ");
    scanf("%d", &a);

    printf("Enter 2nd side : ");
    scanf("%d", &b);

    printf("Enter 3rd side : ");
    scanf("%d", &c);
    if((a+b)>c && (b+c)>a && (c+a)>b){
        printf("Valid Triangle\n");
    }
    else
    {
        printf("Invalid triangle\n");
    }

    return 0;

}