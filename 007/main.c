#include <stdio.h>
#include <math.h>

/* int N = 6; */
int N = 10001;

int main () {
    int p[N];
    p[0] = 2;
    int i = 1;
    int n = 3;
    while (i < N) {
        int isprime = 1;
        for (int k = 0; k < i; k++) {
            if (p[k] > sqrt(n)) {
                break;
            }
            if (n % p[k] == 0) {
                isprime = 0;
            }
        }
        if (isprime == 1) {
            p[i] = n;
            i++;
        }
        n += 2;
    }
    printf("%d\n", p[i - 1]);
    return 0;
}
