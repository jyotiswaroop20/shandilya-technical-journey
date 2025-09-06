#include <stdio.h>

int main()
{
    int num;
    char extra;

    printf("\n");
    printf("This is the program for Checking Leap Year\n\n");
    printf("Enter your Year: ");

  
    if (scanf("%d%c", &num, &extra) != 2 || extra != '\n')
    {
        printf("Error! Invalid Value\n\n");
        return 1;
    }

    // Year validity check
    if (num < 1000)  
    {
        printf("Error! Please enter a valid positive year greater than 999\n\n");
        return 1;
    }

    // Leap year check
    if ((num % 400 == 0) || (num % 4 == 0 && num % 100 != 0))
    {
        printf("This %d is a leap year\n\n", num);
    }
    else
    {
        printf("This %d is not a leap year\n\n", num);
    }

    return 0;
}

