"""Write a C function for unsigned power(double x, unsigned int n) using
minimum number of multiplications. Count the number of multiplications
used."""
#include <stdio.h>

/**
 * Computes x^n using the minimum number of multiplications.
 * Tracks the total multiplication count via a pointer.
 */
double power(double x, unsigned int n, int *multiplication_count) {
    double result = 1.0;
    double current_product = x;
    *multiplication_count = 0;

    // Handle 0^0 mathematical ambiguity safely if required
    if (n == 0) {
        return 1.0;
    }

    while (n > 0) {
        // If n is odd, multiply the current product into the result
        if (n & 1) { // Equivalent to: n % 2 != 0
            result *= current_product;
            (*multiplication_count)++;
        }
        
        // Square the current base for the next bit position
        n >>= 1;    // Equivalent to: n = n / 2
        
        if (n > 0) {
            current_product *= current_product;
            (*multiplication_count)++;
        }
    }

    return result;
}

int main() {
    double x;
    unsigned int n;
    int mult_count = 0;

    printf("Enter base (double) and exponent (unsigned int) separated by space: ");
    if (scanf("%lf %u", &x, &n) != 2) {
        printf("Invalid input.\n");
        return 1;
    }

    double res = power(x, n, &mult_count);

    printf("Result: %lf\n", res);
    printf("Number of multiplications used: %d\n", mult_count);

    return 0;
}
