""" Given a Binary Tree, check if all leaves are at same level or not.
Example 1:
Input:
1
/ \
2 3

Output: 1

Explanation:
Leaves 2 and 3 are at same level.

Example 2:
Input:
10
/ \
20 30
/ \
10 15

Output: 0

Explanation:
Leaves 10, 15 and 30 are not at same level.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(height of tree)
Constraints:
1 ≤ N ≤ 10^3 """

# Check whether all leaf nodes are at same level

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


leaf_level = -1

def check_leaves(root, level):
    global leaf_level

    if root is None:
        return True

    # Leaf node
    if root.left is None and root.right is None:
        if leaf_level == -1:
            leaf_level = level
            return True
        return level == leaf_level

    return (check_leaves(root.left, level + 1) and
            check_leaves(root.right, level + 1))


n = int(input("Enter number of nodes: "))

print("Enter node values level-wise (-1 for NULL):")
values = list(map(int, input().split()))

nodes = []

for val in values:
    if val == -1:
        nodes.append(None)
    else:
        nodes.append(Node(val))

for i in range(n):
    if nodes[i] is not None:
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            nodes[i].left = nodes[left]

        if right < n:
            nodes[i].right = nodes[right]

root = nodes[0]

if check_leaves(root, 0):
    print("Output: 1")
else:
    print("Output: 0")
