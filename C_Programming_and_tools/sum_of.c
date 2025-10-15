#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    system("clear");
    int a;
    int b;
    int sum;
    a = 50;
    b = 60;
    int c;
    c = 2147483645;         // System Type	Typical int Size	Range (Signed)
                               // 16-bit	2 bytes (16 bits)	−32,768 to 32,767
                               // 32-bit	4 bytes (32 bits)	−2,147,483,648 to 2,147,483,647
                               // 64-bit	4 bytes (32 bits)	−2,147,483,648 to 2,147,483,647
    c = c + 5;
    printf("VALUE IS: %d\n",c);

    unsigned int d;
    d = 2147483645; 
    d = d + 5;
    printf("VALUE IS: %u\n",d); //yaha negative range khtam ho gaya unsigned 
    // declear hone par aur unsigned ko print karne ke liye %u use karenge.

    sum = a + b;
    printf("The sum of two numbers is: %d\n",sum);
    printf("Size of INT in memory %lu\n", sizeof(int)); // yaha kisi bhi datatype kitna
    // memory le raha hai usko print ke liye %lu lagate hai

    return 0;
}