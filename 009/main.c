#include <stdio.h>
#include <math.h>

int main () {
    int a, b, c;
    for (a = 1; a < 333; a++) {
        for (b = a + 1; b < 500; b++) {
            c = 1000 - a - b;
            if ((int)pow(a, 2) + (int)pow(b, 2) == (int)pow(c, 2)) {
                goto Find;
                // how about use `break` here?
                // NO. Since break can only break one loop
            }
        }
    }
Find:
    printf("%d\n", a * b * c);
    return 0;
}
