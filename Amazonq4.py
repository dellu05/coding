"""Given a sorted and rotated array A of N distinct elements which is rotated at some point, and
given an element key. The task is to find the index of the given element key in the array A.
Example 1:
Input:
N = 9
A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}
key = 10
Output:
5
Explanation: 10 is found at index 5.
Example 2:
Input:
N = 4
A[] = {3, 5, 1, 2}
key = 6
Output:
-1
Explanation: There is no element that has value 6.
Can you solve it in expected time complexity?
Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 108
1 ≤ key ≤ 108"""

def search_rotated_array(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
            
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1


if __name__ == "__main__":
    n = int(input("Enter number of elements (N): "))
    arr_input = input("Enter array elements separated by spaces: ")
    arr = [int(num) for num in arr_input.split()]
    key = int(input("Enter key to search: "))
    
    result = search_rotated_array(arr, key)
    print(f"Output: {result}")
