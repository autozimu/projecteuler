#include <stdio.h>

int MAX = 4000000;

int main() {
    int n1 = 1;
    int n2 = 1;
    int n3 = n1 + n2;
    int sum = 0;
    while (n3 <= MAX) {
        sum += n3;
        n1 = n2 + n3;
        n2 = n1 + n3;
        n3 = n1 + n2;
    }
    printf("%d\n", sum);
    return 0;
}
