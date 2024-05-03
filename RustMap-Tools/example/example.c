#include <stdio.h>

#define SQUARE(x) ((x) * (x))

void cWorld() {
    printf("Welcome to C world!\n");
}

#define CALL_CWORLD() {cWorld();};

void foo(int a) {
    CALL_CWORLD();
    printf("Square of %d is %d\n", a, SQUARE(a));
}

int main() {
    int num = 5;
    foo(num);
    return 0;
}
