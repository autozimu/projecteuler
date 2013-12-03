#include <stdio.h>
#include <math.h>

int diags() {
    static int n = 1;
    static int d = 1;
    static int i = 0;

    n = n + 2 * d;
    if (i == 3) {
        d++;
        i = 0;
    } else {
        i++;
    }

    return n;
}

int isprime(int n) {
    for (int d = 3; d < sqrt(n)+1; d++) {
        if (n % d == 0) {
            return 0;
        }
    }
    return 1;
}

int main () {
    int nprimes = 0;
    int ndiags = 1;
    while (1) {
        for (int i = 0; i < 4; i++) {
            int n = diags();
            ndiags++;
            if (isprime(n)) {
                nprimes++;
            }
        }
        float ratio = nprimes * 1.0 / ndiags;
        /* printf("%d\t%f\n", (ndiags + 1)/2, ratio); */
        if (ratio < 0.1) {
            break;
        }
    }

    printf("%d\n", (ndiags+1)/2);

    return 0;
}
