#include <stdio.h>
int main() {
    int number, i;
    printf("Enter the number: ");
    scanf("%d", &number);
    printf("Factors of %d are: ", number);
    for (i = 1; i <= number; ++i) {
        if (number % i == 0) {
            printf("%d ", i);
        }
    }
    return 0;
}