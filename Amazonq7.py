""" Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.
Example 1:
Input:
R=4
C=5
M=[[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
Output:
29
Explanation:
The matrix is as follows and the
blue rectangle denotes the maximum sum
rectangle.

Example 2:
Input:
R=2
C=2
M=[[-1,-2],[-3,-4]]
Output:
-1
Explanation:
Taking only the first cell is the
optimal choice.
Expected Time Complexity:O(R*R*C)
Expected Auxillary Space:O(R*C)
Constraints:
1<=R,C<=500
-1000<=M[i][j]<=1000 """

# Maximum Sum Submatrix

def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter matrix elements row-wise:")

matrix = []
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

max_sum = float('-inf')

for left in range(c):

    temp = [0] * r

    for right in range(left, c):

        for i in range(r):
            temp[i] += matrix[i][right]

        current_sum = kadane(temp)

        if current_sum > max_sum:
            max_sum = current_sum

print("Maximum Sum Submatrix =", max_sum)
