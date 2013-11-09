#include <stdio.h>
#include <math.h>

int pantagon(int i) {
    return i * (3 * i - 1) / 2;
}

int ispantagon(int p) {
    long n = lround((1 + sqrt(1 + 24 * p)) / 6);
    return n * (3 * n - 1) / 2 == p;
}

int main () {
    int i = 1900;
    int found = 0;
    while (!found) {
        i++;
        int j = 1;
        while (pantagon(i) >= 3 * j + 1) {
            printf("%d\t%d\n", i, j);
            if (ispantagon(pantagon(i) + pantagon(j)) && ispantagon(pantagon(i) + 2 * pantagon(j))) {
                printf("%d\n", i);
                found = 1;
                break;
            }
            j++;
        }
    }
    return 0;
}
