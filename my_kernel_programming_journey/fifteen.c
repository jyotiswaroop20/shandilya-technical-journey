#include <stdio.h>
int main()
{
	int l;
	int w;
	char extra;
	printf("\n\n");
	printf("This Program is for calculating area of rectangle so enter only integer number\n\n");
	printf("Enter your length: ");
	if (scanf("%d%c", &l, &extra) != 2 || extra != '\n')
	{
		 printf("Error! Invalid Value\n\n");
       		 return 1;
	}
	printf("Enter your width: ");
	if (scanf("%d%c", &w, &extra) != 2 || extra != '\n')
	{
		 printf("Error! Invalid Value\n\n");
                 return 1;
	}
	else
	{
		int area = l * w;
		printf("The Area of Recteangle is - %d\n\n", area);
		
	}

}
