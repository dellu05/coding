""" Given an integer array of which both first half and second half are sorted.
Write a function to merge the two parts to create one single sorted array
in place [do not use any extra space]. Eg: If input array is { 2, 3, 8, -1, 7,
10 } then Output should be -1, 2, 3, 7, 8, 10."""

def merge_in_place(arr):
    n = len(arr)
    
    # 1. Find the starting index of the second sorted half
    mid = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            mid = i + 1
            break
    else:
        return  # Array is already fully sorted
        
    # 2. In-place merge using two pointers
    i = 0        # Pointer for the first half
    j = mid      # Pointer for the second half
    
    while i < j and j < n:
        if arr[i] <= arr[j]:
            i += 1
        else:
            # Save the value and shift elements to the right
            value = arr[j]
            k = j
            while k > i:
                arr[k] = arr[k - 1]
                k -= 1
            
            # Place the smaller element at its correct sorted position
            arr[i] = value
            
            # Advance boundaries forward
            i += 1
            j += 1

def main():
    print("Example input format: 2 3 8 -1 7 10")
    user_input = input("Enter numbers separated by spaces: ")
    
    try:
        # Convert input string into a list of integers
        input_arr = [int(x) for x in user_input.split()]
        
        if not input_arr:
            print("The array is empty.")
            return
            
        print(u"\nOriginal Array: \u200e", input_arr)
        
        # Modify the array in place
        merge_in_place(input_arr)
        
        print("Sorted Array:   ", input_arr)
        
    except ValueError:
        print("Error: Please enter integers separated by single spaces only.")

if __name__ == '__main__':
    main()
