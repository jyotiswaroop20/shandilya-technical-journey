#include <stdio.h>
int main(void) {
    int a = 999;
    char b = 'H';

    // %zu format specifier hai size_t print karne ke liye
    printf("%zu\n", sizeof a);       // Output: 4 (mere system pe)
    printf("%zu\n", sizeof(2 + 7));  // Output: 4 (int ka size)
    printf("%zu\n", sizeof 3.14);    // Output: 8 (double ka size)
    printf("%zu\n" , sizeof b);
    printf("%zu\n", sizeof(int));
    printf("%zu\n", sizeof(char));    
    return 0;
}
