#include <stdio.h>
#include <math.h>

/* int N = 13195; */
long N = 600851475143;

int main() {
    for (int i = 2; i <= sqrt(N); i++) {
        while (N % i == 0) {
            N /= i;
        }
    }
    printf("%ld\n", N);
    return 0;
}
