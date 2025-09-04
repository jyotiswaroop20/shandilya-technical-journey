#include <stdio.h>
int main()
{
        int dividend;
	int divisor; 
        printf("\n");
        
	printf("Enter the value of Dividend: ");
	if (scanf("%d", &dividend) !=1)
	{
		printf("Invalid input! Please enter an integer.\n");
        	return 1;
	}
	
	printf("Enter the value of Divisor: ");
	if (scanf("%d", &divisor) != 1)
       	{
       	 	printf("Invalid input! Please enter an integer.\n");
        	return 1;
    	}
	
	if(dividend < divisor)
	{
		printf("\n");
		printf("Error! Dividend should not be less then divisor\n\n");
		return 1;
	}
	
	if (divisor == 0) 
	{
       			printf("\nError! Divisor cannot be zero.\n\n");
        		return 1;
    	}
	else
	{	
		int remainder = dividend % divisor;
		printf("The Remainder is: %d\n\n", remainder);		
	}
		return 0;
}
