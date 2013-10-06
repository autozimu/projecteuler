#include <stdio.h>

int main () {
    int ndays[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int d = 2; // 1 Jan, 1901 is Tuesday
    int isleap = 0;
    int nsun = 0;
    for (int year = 1901; year <= 2000; year++) {
        if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) {
            isleap = 1;
            ndays[1] = 29;
        }

        for (int i = 0; i < 12; i++) {
            d += ndays[i];
            d %= 7;
            if (d == 0) {
                nsun++;
            }
        }

        if (isleap == 1) {
            ndays[1] = 28;
        }
    }

    printf("%d\n", nsun);
    return 0;
}
