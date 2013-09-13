#include <stdio.h>

int MAX = 1000 - 1;

// sum of multiples of n
int summultiples(int n) {
    // number of ns
    int nn = MAX / n;
    return n * nn * (nn + 1) / 2;
}

int main() {
    printf("%d\n", summultiples(3) + summultiples(5) - summultiples(15));
    return 0;
}
