#include <stdio.h>
#include <math.h>

/* int N = 10; */
int N = 2000000;

int main () {
    int p[N];
    for (int i = 0; i < N; i++) {
        p[i] = 1;
    }
    p[0] = p[1] = 0;
    int i = 2;
    int k;
    do {
        k = i * i;
        do {
            p[k] = 0;
            k += i;
        } while (k < N);
        do {
            i++;
        } while (p[i] == 0);
    } while (i <= sqrt(N));
    long sum = 0;
    for (int i = 0; i < N; i++) {
        if (p[i] == 1) {
            sum += i;
        }
    }
    printf("%ld\n", sum);
    return 0;
}
