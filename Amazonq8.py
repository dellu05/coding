""" Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right
pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The
order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder
traversal (leftmost node in BT) must be the head node of the DLL.

Example 1:
Input:
1
/ \
3 2
Output:
3 1 2
2 1 3
Explanation: DLL would be 3<=>1<=>2
Example 2:
Input:
10
/ \
20 30
/ \
40 60
Output:
40 20 60 10 30
30 10 60 20 40

Explanation: DLL would be
40<=>20<=>60<=>10<=>30.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree and this space is used implicitly for the recursion stack.
Constraints:
1 ≤ Number of nodes ≤ 105
0 ≤ Data of a node ≤ 105 """

# Binary Tree to Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


prev = None
head = None

def convert_to_dll(root):
    global prev, head

    if root is None:
        return

    convert_to_dll(root.left)

    if prev is None:
        head = root
    else:
        prev.right = root
        root.left = prev

    prev = root

    convert_to_dll(root.right)


# Input Tree
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

convert_to_dll(root)

# Forward Traversal
print("DLL Forward:")
temp = head
last = None

while temp:
    print(temp.data, end=" ")
    last = temp
    temp = temp.right

print()

# Backward Traversal
print("DLL Backward:")

while last:
    print(last.data, end=" ")
    last = last.left
