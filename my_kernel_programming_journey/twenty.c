#include <stdio.h>
#include <stdlib.h>
int main(void)
{

	int i;
	int j;
	printf("\n");
	printf("Syste Uptime after every 5 seonds\n");
	for(i =0, j=1; i<10; i++ , j++)
	{
		system("sleep 5");
		printf("%d\n",j);
		printf("%d\n" ,j*2);
		system("uptime \n");
	}
	return 0;
}
