#include <stdio.h>

/* int N = 10; */
int N = 100;

int main () {
    long long factorial = 1;
    for (int i = 2; i <= N; i++) {
        factorial *= i;
    }

    if (factorial <= 0) {
        printf("ERROR: exceed data type capacity!\n");
        return 0;
    }

    int sum = 0;
    do {
        sum += factorial % 10;
        factorial /= 10;
    } while (factorial != 0);

    printf("%d\n", sum);
    return 0;
}
