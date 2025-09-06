#include <stdio.h>
int main()
{
    int a, b, c;
    char extra;

    printf("\nThis is the program for Checking greater number in three numbers\n\n");

    printf("Enter your first integer number: ");
    if (scanf("%d%c", &a, &extra) != 2 || extra != '\n')
    {
        printf("Error! Invalid Value\n\n");
        return 1;
    }

    printf("Enter your second integer number: ");
    if (scanf("%d%c", &b, &extra) != 2 || extra != '\n')
    {
        printf("Error! Invalid Value\n\n");
        return 1;
    }

    printf("Enter your third integer number: ");
    if (scanf("%d%c", &c, &extra) != 2 || extra != '\n')
    {
        printf("Error! Invalid Value\n\n");
        return 1;
    }

    if (a > b && a > c)
    {
        printf("%d is the greater number\n\n", a);
    }
    else if (b > a && b > c)
    {
        printf("%d is the greater number\n\n", b);
    }
    else if (c > a && c > b)
    {
        printf("%d is the greater number\n\n", c);
    }
    else if (a == b && a == c)
    {
        printf("All numbers are equal\n\n");
    }
    else if (a == b && a != c)
    {
        if (a > c)
            printf("%d is the greater number\n\n", a);
        else
            printf("%d is the greater number\n\n", c);
    }
    else if (a == c && a != b)
    {
        if (a > b)
            printf("%d is the greater number\n\n", a);
        else
            printf("%d is the greater number\n\n", b);
    }
    else if (b == c && b != a)
    {
        if (b > a)
            printf("%d is the greater number\n\n", b);
        else
            printf("%d is the greater number\n\n", a);
    }

    return 0;
}
