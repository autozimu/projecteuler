#include <stdio.h>
#include <math.h>

/* int N = 10; */
int N = 2000000;

int main () {
    int p[N];
    p[0] = 2;
    int i = 1;
    for (int n = 3; n < N; n += 2) {
        int isprime = 1;
        for (int k = 0; k < i; k++) {
            if (p[k] > sqrt(n)) {
                break;
            }
            if (n % p[k] == 0) {
                isprime = 0;
                break;
            }
        }
        if (isprime == 1) {
            /* printf("%d\n", n); */
            p[i] = n;
            i++;
        }
    }
    long sum = 0;
    for (int k = 0; k < i; k++) {
        sum += p[k];
    }
    printf("%ld\n", sum);
    return 0;
}
