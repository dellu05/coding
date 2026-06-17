"""    3. Gofrugal
Decimal to binary
Write a C program to convert a decimal number to binary and 
print the count of 1's in it. If 1's are not present in binary number, then print invalid input."""
#include <stdio.h>

int main() {
    int n, count = 0;
    int binary[32]; 
    int i = 0;
    printf("Enter a decimal number: ");
    if (scanf("%d", &n) != 1) {
        printf("invalid input\n");
        return 0;
    }
    if (n <= 0) {
        printf("invalid input\n");
        return 0;
    }
    int temp = n;
    while (temp > 0) {
        binary[i] = temp % 2;  
        if (binary[i] == 1) {
            count++;           
        }
        temp = temp / 2;       
        i++;
    }
    if (count == 0) {
        printf("invalid input\n");
    } else {
        printf("Binary representation: ");
        for (int j = i - 1; j >= 0; j--) {
            printf("%d", binary[j]);
        }
        printf("\nCount of 1's: %d\n", count);
    }
    return 0;
}
