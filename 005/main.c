#include <stdio.h>
#include <math.h>

int N = 20 + 1;

int main() {
    int midx[N];
    // initalization
    for (int i = 0; i < N; i++) {
        midx[i] = 0;
    }

    // prime factor
    for (int n = 2; n < N; n++) {
        int idx[N];
        for (int i = 0; i < N; i++) {
            idx[i] = 0;
        }
        int nn = n;
        for (int f = 2; f <= sqrt(nn); f++) {
            while (nn % f == 0) {
                idx[f]++;
                nn /= f;
            }
        }
        if (nn != 1) {
            idx[nn] += 1;
        }

        for (int i = 0; i < N; i++) {
            if (idx[i] > midx[i]) {
                midx[i] = idx[i];
            }
        }
    }

    // multiplication
    int m = 1;
    for (int i = 1; i < N; i++) {
        m *= (int)pow(i, midx[i]);
    }

    printf("%d\n", m);
    return 0;
}
