#include <stdio.h>
#include <math.h>
#define N 28124

int main () {
    int numbers[N];
    for (int n = 0; n < N; n++) {
        numbers[n] = 0;
    }

    for (int n = 1; n < N; n++) {
        int divisor_sum = 1;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                divisor_sum += i;
            }
        }
        if (divisor_sum > n) {
            numbers[n] = 1;
        }
    }

    int sum = 0;
    for (int n = 1; n < N; n++) {
        int abundant_sum = 0;
        for (int i = 12; i <= n/2; i++) {
            if (numbers[i] == 1 && numbers[n - i] == 1) {
                abundant_sum = 1;
                break;
            }
        }
        if (abundant_sum == 0) {
            /* printf("%d\n", n); */
            sum += n;
        }
    }
    printf("%d\n", sum);
    return 0;
}
