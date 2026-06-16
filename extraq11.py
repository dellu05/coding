#Detect if two integers have opposite signs (using bitwise operator)
def have_opposite_signs(a, b):
    # Returns True if a and b have opposite signs
    return (a ^ b) < 0

def main():
    print("Example input: -5 10")
    user_input = input("Enter two integers separated by a space: ")
    
    try:
        num1, num2 = map(int, user_input.split())
        
        # Check if either of the numbers is zero, as 0 technically doesn't have a sign
        if num1 == 0 or num2 == 0:
            print("Note: One of the inputs is 0 (which is neither positive nor negative).")
            
        if have_opposite_signs(num1, num2):
            print(f"Yes! {num1} and {num2} have OPPOSITE signs.")
        else:
            print(f"No. {num1} and {num2} have the SAME sign.")
            
    except ValueError:
        print("Error: Please enter exactly two valid integers separated by a space.")

if __name__ == '__main__':
    main()
