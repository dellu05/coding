#Write a program to check an integer is a power of 2 (using bitwise operator)
def is_power_of_two(n):
    # Powers of 2 must be strictly greater than 0
    # n & (n - 1) clears the lowest set bit. If it becomes 0, it's a power of 2.
    return n > 0 and (n & (n - 1)) == 0

def main():
    print("Example input: 16")
    user_input = input("Enter an integer: ")
    
    try:
        num = int(user_input)
        
        if is_power_of_two(num):
            print(f"Yes! {num} is a power of 2.")
        else:
            print(f"No. {num} is NOT a power of 2.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == '__main__':
    main()
