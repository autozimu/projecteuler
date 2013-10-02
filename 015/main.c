#include <stdio.h>

/* int N = 2; */
int N = 20;

int main () {
    long double nroutes = 1; // number of routes
    // NOTE: the data type can not be integer, even long long integer is not
    // enough. If we use integer here, we will have to first calculate 2n *
    // (2n - 1) * ... * (n + 1), it might possibly exceed the maximum capacity
    // of long long integer.
    for (int i = 1; i <= N; i++) {
        nroutes *= (N + i) / (1.0 * i);
    }
    // NOTE for the (1.0 *), or the integer division will be truncated.

    printf("%Lf\n", nroutes);
    return 0;
}
