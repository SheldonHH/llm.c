#include <stdio.h>

void iamfunction() {
    printf("This is Function!\n"); 
}

#define IAMMACRO() printf("I'm Macro ! \n")

// type 1: Simple macro for arithmetic expressions
#define SQUARE(x) ((x) * (x))

// type 2: Macro for calling a user-defined function
#define CALL_Func() iamfunction()

// type 3: Macro that only involves another macro call
#define CALL_MACRO() IAMMACRO()

// type 4: Replacing a complex macro with a function to improve readability and maintainability
void COMBINED() {
    iamfunction();
    IAMMACRO();
}

int main() {
    int num = 5;
    int square = SQUARE(num); // Calculate square of num
    CALL_Func();              // Call the function via macro
    CALL_MACRO();             // Call another macro
    COMBINED();               // Execute the combined function
    return 0;
}
