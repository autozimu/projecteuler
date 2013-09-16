#include <stdio.h>
#include <math.h>

/* int N = 10; */
int N = 100;

int main() {
    printf("%d\n", (int)pow((N * (N + 1) / 2), 2) - N * (N + 1) * (2 * N + 1) / 6);
    return 0;
}
