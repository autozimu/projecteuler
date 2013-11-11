#include <stdio.h>
#include <math.h>
#define N 1000000
#define targetnfactors 4

// allocate prime sieve
int sieve[N];

// return number of prime factors
int nfactors(n) {
    int npf = 0;
    for (int i = 2; i < sqrt(n) + 1; i++) {
        if (sieve[i] == 1 && n % i == 0) {
            npf++;
            while (n % i == 0) {
                n /= i;
            }
        }
    }
    if (n != 1) {
        npf++;  // should be a prime, and itself is one of the factor
    }
    return npf;
}

int main() {
    // initialize prime sieve
    for (int i = 0; i < N; i++) {
        sieve[i] = 1;
    }
    sieve[0] = sieve[1] = 0;
    for (int d = 2; d < sqrt(N) + 1; d++) {
        for (int i = 2 * d; i < N; i += d) {
            sieve[i] = 0;
        }
    }

    int n = 210;
    int counter = 0;
    while (1) {
        n++;
        /* printf("%d\n", n); */
        if (nfactors(n) == targetnfactors) {
            counter++;
        } else {
            counter = 0;
        }
        if (counter == targetnfactors) {
            break;
        }
    }

    return 0;
}
