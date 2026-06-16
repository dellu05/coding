""" Add 2 numbers without using arithmetic operators. """


def add_without_arithmetic(a, b):
    # 32-bit mask to handle negative numbers and avoid infinite loops in Python
    mask = 0xFFFFFFFF
    
    while b != 0:
        # 1. Find the carry bits
        carry = (a & b) & mask
        
        # 2. Add bits without carrying
        a = (a ^ b) & mask
        
        # 3. Shift the carry to the left
        b = (carry << 1) & mask
    
    # If the result is a negative 32-bit signed integer, convert it back to Python's format
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

def main():
    print("Example input: 15 27")
    user_input = input("Enter two integers separated by a space: ")
    
    try:
        num1, num2 = map(int, user_input.split())
        result = add_without_arithmetic(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter exactly two valid integers separated by a space.")

if __name__ == '__main__':
    main()
