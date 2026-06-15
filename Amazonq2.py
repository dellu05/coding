"""Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs cannot contain duplicate Nodes.
A BST is defined as follows:
• The left subtree of a node contains only nodes with keys less than the node's key.
• The right subtree of a node contains only nodes with keys greater than the node's key.
• Both the left and right subtrees must also be binary search trees.
Example 1:
Input:
2
/ \
1 3
Output: 1
Explanation:
The left subtree of root node contains node
with key lesser than the root nodes key and
the right subtree of root node contains node
with key greater than the root nodes key.
Hence, the tree is a BST.
Example 2:
Input:
2
\
7
\
6
\
5
\
9
\
2
\
6
Output: 0
Explanation:
Since the node with value 7 has right subtree
nodes with keys less than 7, this is not a BST.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the BST).
Constraints:
0 <= Number of edges <= 100000
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
