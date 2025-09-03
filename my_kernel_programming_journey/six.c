#include<stdio.h>
int main()
{
        printf("\n");
	printf("This Program is for calculating area of circle.....\n\n");
        float r ;
        printf("Enter your Number: ");
        scanf("%f", &r);
        float pi = 3.1415;
        float A = pi * r * r;
        printf("The Area of circle is : %f\n\n", A);
        return 0;
}

