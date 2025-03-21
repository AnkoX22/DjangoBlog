#include <stdio.h>
#include <stdlib.h>


int main(void) {

    int number1, number2;

    printf("%s", "Enter the first number: ");
    scanf("%d", &number1);
    printf("%s", "Enter the second number: ");
    scanf("%d", &number2);

    printf("/n%d + %d = %d", number1, number2, number1+number2);
    printf("/n%d - %d = %d", number1, number2, number1-number2);
    printf("/n%d / %d = %d", number1, number2, number1/number2);
    printf("/n%d * %d = %d", number1, number2, number1*number2);

    return 0;
}