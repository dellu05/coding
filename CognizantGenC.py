"""    2. Cognizant GenC
Lucky number
Problem Statement – Chaman planned to choose a four digit lucky number for his car. His lucky numbers are 3,5 and 7. Help him find the number, whose sum is divisible by  3 or 5 or 7. Provide a valid car number, Fails to provide a valid input then display that number is not a valid car number. 
Note : The input other than 4 digit positive number[includes negative and 0] is considered as invalid.
Refer the samples, to read and display the data.
Sample Input 1:
    • Enter the car no:1234
Sample Output 1:
    • Lucky Number
Sample Input 2:
    • Enter the car no:1214
Sample Output 2:
    • Sorry its not my lucky number
Sample Input 3:
    • Enter the car no:14
Sample Output 3:
    • 14 is not a valid car number"""
car_input = input("Enter the car no:")
if car_input.isdigit():
    num = int(car_input)
    if 1000 <= num <= 9999:
        digit_sum = 0
        for digit in car_input:
            digit_sum += int(digit)
        if digit_sum % 3 == 0 or digit_sum % 5 == 0 or digit_sum % 7 == 0:
            print("Lucky Number")
        else:
            print("Sorry its not my lucky number")
    else:
        print(f"{car_input} is not a valid car number")
else:
    print(f"{car_input} is not a valid car number")
