#include <stdio.h>
#define N 10000

int main () {
    int d[N];
    for (int n = 1; n < N; n++) {
        for (int i = 1; i <= n/2; i++) {
            if (n % i == 0) {
                d[n] += i;
            }
        }
    }

    int sum = 0;
    for (int n = 1; n < N; n++) {
        if (d[n] != n && d[n] >= 1 && d[n] < N && d[d[n]] == n){
            printf("d(%d) = %d, d(%d) = %d\n", n, d[n], d[n], d[d[n]]);
            sum += n;
            sum += d[n];
        }
    }
    sum /= 2;

    printf("%d\n", sum);
    return 0;
}
