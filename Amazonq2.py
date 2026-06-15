"""Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing
order, and a number X is given. The task is to find whether element X is present in the matrix
or not.
Example 1:
Input:
N = 3, M = 3
mat[][] = 3 30 38
44 52 54
57 60 69
X = 62
Output
0
Explanation:
62 is not present in the
matrix, so output is 0
Example 2:
Input:
N = 1, M = 6
mat[][] = 18 21 27 38 55 67
X = 55
Output:
1
Explanation:
55 is present in the
matrix at 5th cell.
Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(1).
Constraints:
1 <= N, M <= 1005
1 <= mat[][] <= 10000000
1<= X <= 10000000
"""
def search_matrix(mat, n, m, x):
    row = 0
    col = m - 1
    while row < n and col >= 0:
        current = mat[row][col]
        if current == x:
            return 1
        elif current > x:
            col -= 1
        else:
            row += 1
    return 0


if __name__ == "__main__":
    n = int(input("Enter number of rows (N): "))
    m = int(input("Enter number of columns (M): "))
    matrix = []
    for i in range(n):
        row_input = input(f"Row {i + 1}: ")
        row_elements = [int(num) for num in row_input.split()]
        matrix.append(row_elements)
    x = int(input("Enter the number to find (X): "))
    result = search_matrix(matrix, n, m, x)
    print(f"Output: {result}")
