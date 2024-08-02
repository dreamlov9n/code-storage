#include <stdio.h>
#include <stdlib.h>
//
//
int main()
{
    float cel;

    printf("Celsius to Fahrenheit Launched! Press enter.\n");

    getchar(); //the same as input() in py (waiting for any input)
    system("clear"); // clear da screenuh!!

    printf("Please tell me the Celsius value:");
    scanf("%f", &cel);
    printf("\nGiven value: %0.1f", cel);

    float fah=(cel * 1.8)+32; //C to F formula

    printf("\n\n%0.1f to Fahrenheit equals %0.1f",cel,fah);
    return 0;
}