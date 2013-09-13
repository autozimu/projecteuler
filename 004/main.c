#include <stdio.h>

int main() {
    int lp = 0;
    for (int m = 100; m <= 999; m++) {
        for (int n = m; n <= 999; n++) {
            int p = m * n;

            int ispalindrome = 1;
            char s[20];
            char *i, *j;
            sprintf(s, "%d", p);
            i = j = s;
            // move pointer j to the end
            while (*j) {
                j++;
            }
            j--;
            for (; i < j; i++, j--) {
                if (*i != *j) {
                    ispalindrome = 0;
                }
            }

            if (ispalindrome && p > lp) {
                lp = p;
            }
        }
    }
    printf("%d\n", lp);
    return 0;
}
