#include <stdio.h>

int MAX = 4000000;

int main() {
    int n1 = 0;
    int n2 = 2;
    int tmp;
    int sum = 0;
    while (n2 <= MAX) {
        sum += n2;
        tmp = n2;
        n2 = 4 * n2 + n1;
        n1 = tmp;
    }

    printf("%d\n", sum);
    return 0;
}
