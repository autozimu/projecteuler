#include <stdio.h>

int N = 1000000;

int main () {
    int nsequence;  // number of terms in the sequence
    int mnsequence = 1;  // max number of terms
    int largestn = 1;  // the number when max number of terms
    for (int n = 1; n < N; n++) {
        nsequence = 1;
        long tempn = n;
        while (tempn != 1) {
            if (tempn % 2 == 0) {
                tempn /= 2;
            } else {
                tempn = 3 * tempn + 1;
            }
            nsequence++;
        }

        if (mnsequence < nsequence) {
            mnsequence = nsequence;
            largestn = n;
        }

        /* printf("%d\t%d\n", n, nsequence); */
    }

    printf("%d\n", largestn);

    return 0;
}
