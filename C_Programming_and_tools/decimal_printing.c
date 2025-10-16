#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int a = 0134; //(octal number)
    int b = 0x3a5; //(hexadecimal) a=10, b=11 , c=12
    printf("%d\n", a); //result would be = 92
    printf("%d\n", b); //result would be = 933

    printf("%d\n", a + b);
    return 0;
}