#include <stdio.h>
int main() {
    unsigned long sum = 0, t1 = 0, t2 = 1, t3 = 2, i;

    while (t3 < 4000000) {
        t3 = t1 + t2;
        if(t3 % 2 == 0) {
            sum = sum + t3;
        }
        t1 = t2;
        t2 = t3;
    }

    printf("%lu\n", sum);
    return 0;
}
