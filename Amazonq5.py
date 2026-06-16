
""" Given the root of a binary tree. Check whether it is a BST or not.
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
0 <= Number of edges <= 100000 """ 

def check_bst(arr, index, min_val, max_val):
    if index >= len(arr) or arr[index] is None:
        return True

    if arr[index] <= min_val or arr[index] >= max_val:
        return False

    return (check_bst(arr, 2 * index + 1, min_val, arr[index]) and
            check_bst(arr, 2 * index + 2, arr[index], max_val))


n = int(input("Enter number of nodes: "))

print("Enter node values level-wise (-1 for NULL):")
arr = []

for i in range(n):
    x = int(input())
    if x == -1:
        arr.append(None)
    else:
        arr.append(x)

if check_bst(arr, 0, float('-inf'), float('inf')):
    print("Output: 1")
else:
    print("Output: 0")
