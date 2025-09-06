#include <stdio.h>
int main()
{
	int num;
	char extra;
	printf("\n");
	printf("This is the program for Verify Even and Odd\n\n");
	printf("Enter your number: ");
	if (scanf("%d%c", &num, &extra) != 2 || extra != '\n')
	{
		printf("Error! Invalid Value\n\n");
		return 1;
	}	
	if(num % 2 == 0)
	{
		printf("This %d is Even Number\n\n", num);
	}
	else
	{
		printf("This %d odd Number\n\n", num);
	}

	return 0;
}
