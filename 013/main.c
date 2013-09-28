#include <stdio.h>

int main () {
    int b[100][50];
    FILE *f;
    f = fopen("b.txt", "r");
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 50; j++) {
            fscanf(f, "%1d", &b[i][j]);
        }
    }
    fclose(f);

    int carry = 0;
    int sum = 0;
    for (int j = 12 - 1; j >= 0; j--) {
        sum = 0;
        for (int i = 0; i < 100; i++) {
            sum += b[i][j];
        }
        sum += carry;
        /* printf("%d\t", sum); */
        carry = sum / 10;
        sum %= 10;
        printf("%d", sum);
        /* printf("%d\t%d\n", carry, sum); */
    }
    printf("\n");
    printf("%d\n", carry);

    return 0;
}
