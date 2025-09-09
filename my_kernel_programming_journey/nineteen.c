#include <stdio.h>
int main(void)
{
	int num;
	printf("Enter your integer Value: ");
	scanf("%d" , &num);
	if(num > 10)
	{
		num += 20;
		printf("apka input 10 se jyada hai isliye ye value 20 jodkar aaya %d\n\n", num);
	}
	else
	{
		num += 40;
		printf("apka input 10 se kam hai isliye ye value 40 jodkar aaya %d\n\n", num);
	}
}
