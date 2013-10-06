#include <stdio.h>
/* #define N 15 */
#define N 15
#define max(x, y)  ((x > y) ? x : y)

int b[N][N];

int main () {
    FILE *f;
    f = fopen("b.txt", "r");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= i; j++) {
            fscanf(f, "%d", &b[i][j]);
        }
    }
    fclose(f);

    for (int i = N - 2; i >= 0; i--) {
        for (int j = 0; j <= i; j++) {
            b[i][j] += max(b[i + 1][j], b[i + 1][j + 1]);
        }
    }

    printf("%d\n", b[0][0]);
    return 0;
}
