#include <stdio.h>

int makeChange(int n, int d) {
    if (n < 0) {
        return 0;
    } else if (n == 0) {
        return 0;
    } else {
        int sum = 0;
        switch (d) {
            case 25:
                sum += makeChange(n - 25, 25);
            case 10:
                sum += makeChange(n - 10, 10);
            case 5:
                sum += makeChange(n - 5, 5);
            case 1:
                sum++;
        }
        return sum;
    }
}

int main () {
    printf("%d\n", makeChange(6, 25));
    return 0;
}
