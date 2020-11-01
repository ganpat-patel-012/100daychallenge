#include <stdio.h>
int main() {
    int i, n, t1 = 0, t2 = 1, next;
    printf("Enter number of elemts you want to print: ");
    scanf("%d", &n);
    printf("Fibonacci Series (first %d elements): ",n);

    for (i = 1; i <= n; ++i) {
        printf("%d, ", t1);
        next = t1 + t2;
        t1 = t2;
        t2 = next;
    }

    return 0;
}