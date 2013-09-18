#include <stdio.h>
#include <math.h>

/* int N = 10; */
int N = 2000000;

int main () {
    long sum = 2;
    for (int n = 3; n < N; n += 2) {
        int isprime = 1;
        for (int k = 2; k <= sqrt(n); k++) {
            if (n % k == 0) {
                isprime = 0;
                break;
            }
        }
        if (isprime == 1) {
            /* printf("%d\n", n); */
            sum += n;
        }
    }
    printf("%ld\n", sum);
    return 0;
}
