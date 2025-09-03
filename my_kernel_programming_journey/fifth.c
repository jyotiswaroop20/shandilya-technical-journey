#include<stdio.h>
int main()
{
	printf("\n");
	float r ;
	printf("Enter your Number: ");
	scanf("%f", &r);
	float pi = 3.1415;
	float v = (4 * pi * r * r * r) / 3;
	printf("The Volume of sphere is : %f\n\n", v);
	return 0;
}
