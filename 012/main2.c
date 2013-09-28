#include <stdio.h>

/* int N = 5; */
int N = 500;

int main () {
    // array of prime numbers
    int p[100 * N];
    p[0] = 2;
    int np = 1; // number of prime numbers
    int pm = 2; // largest prime number, prime max

    int n = 1;
    int idx[100 * N];
    int nd; // number of divisors

    do {
        n++;
        if (n + 1 > pm) {
            // find next prime number
            int nextp = n;
            int isprime;
            do {
                nextp += 1;
                isprime = 1;
                for (int i = 0; i < np; i++) {
                    if (nextp % p[i] == 0) {
                        isprime = 0;
                    }
                }
            } while (isprime == 0);
            p[np] = pm = nextp;
            np++;
        }


        // initialize index
        for (int i = 0; i < np; i++) {
            idx[i] = 0;
        }

        // get index
        int temp = n;
        for (int i = 0; i < np; i++) {
            while (temp % p[i] == 0) {
                idx[i]++;
                temp /= p[i];
            }
        }
        temp = n + 1;
        for (int i = 0; i < np; i++) {
            while (temp % p[i] == 0) {
                idx[i]++;
                temp /= p[i];
            }
        }
        idx[0]--; // consider the factor 1/2

        nd = 1;
        for (int i = 0; i < np; i++) {
            nd *= idx[i] + 1;
        }

        /* printf("%d\t%d\n", n, nd); */
    } while (nd <= N);


    printf("%d\n", n * (n + 1) / 2);
    return 0;
}
