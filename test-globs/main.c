#include <stdio.h>
#include "wrong_example.h"
#include "second.c"

int main() {
    printf("The value of myGlobalInt is %d\n", myGlobalInt);
    printGlobalIntSecond();
    return 0;
}
