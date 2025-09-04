#include <stdio.h>
int main()
{
	int p,q;
	printf("\n");
	printf("Enter the value of p and q: ");
	if (scanf("%d %d", &p,&q) != 2)
	{
		
		printf("Error! enter only integer value\n\n");
		return 1;
	}
	else
	{
		printf("\n\n");	
	        printf("Good! now this is the right value, see the result below---");
		printf("\n\n");
		printf("p = %d q = %d", p,q);
		printf("\n\n");
	}
	return 0;
}
