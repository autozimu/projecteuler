#include <stdio.h>

/* int N = 5; */
int N = 500;

int ndivisors (int t) {
    int nd = 0;
    for (int i = 1; i <= t; i++) {
        if (t % i == 0) {
            nd++;
        }
    }
    return nd;
}


int main () {
    int n = 0;
    int t;
    int nd;
    do {
        n++;
        t = n * (n + 1) / 2;
        nd = ndivisors(t);
        printf("%d\t%d\n", n, nd);
    } while (nd <= N);

    printf("%d\n", t);
    return 0;
}
