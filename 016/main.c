#include <stdio.h>

/* int N = 15; */
int N = 1000;

int main() {
    int power[N];
    for (int i = 0; i < N; i++) {
        power[i] = 0;
    }
    power[0] = 2;
    int carry = 0;
    for (int j = 0; j < 333; j++) {
        for (int i = 0; i < N; i++) {
            power[i] = power[i] * 8 + carry;
            carry = power[i] / 10;
            power[i] %= 10;
        }
        /* for (int i = 0; i < N; i++) { */
            /* printf("%d\t", power[i]); */
        /* } */
        /* printf("\n"); */
    }

    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += power[i];
    }
    printf("%d\n", sum);
    return 0;
}
