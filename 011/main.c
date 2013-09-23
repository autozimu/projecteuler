#include <stdio.h>

int main () {
    int b[20][20];
    int maxmul = 0;

    // read in buffer
    FILE *fp;
    fp = fopen("b.txt", "r");
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 20; j++) {
            fscanf(fp, "%d", &b[i][j]);
        }
    }
    fclose(fp);

    for (int i = 0; i <= 20 - 4; i++) {
        for (int j = 0; j <= 20 - 4; j++) {
            int mul11 = b[i][j] * b[i + 1][j] * b[i + 2][j] * b[i + 3][j];
            int mul22 = b[i][j] * b[i][j + 1] * b[i][j + 2] * b[i][j + 3];
            int mul12 = b[i + 3][j] * b[i + 2][j + 1] * b[i + 1][j + 2] * b[i][j + 3];
            int mul21 = b[i][j] * b[i + 1][j + 1] * b[i + 2][j + 2] * b[i + 3][j + 3];
            if (mul11 > maxmul) {
                maxmul = mul11;
            }
            if (mul22 > maxmul) {
                maxmul = mul22;
            }
            if (mul12 > maxmul) {
                maxmul = mul12;
            }
            if (mul21 > maxmul) {
                maxmul = mul21;
            }
        }
    }
    // whoops, it seems we did not check the horizontal/vertical product of
    // the last three rows/columns ...

    printf("%d\n", maxmul);

    return 0;
}
