# Merge two binary trees into one.

#A  summing up
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes_input):
    """Builds a binary tree from a space-separated string of values."""
    if not nodes_input or nodes_input[0].lower() == 'null':
        return None
    
    nodes = [None if x.lower() == 'null' else TreeNode(int(x)) for x in nodes_input]
    root = nodes[0]
    queue = deque([root])
    front = 1
    
    while queue and front < len(nodes):
        node = queue.popleft()
        if node:
            if front < len(nodes):
                node.left = nodes[front]
                front += 1
                queue.append(node.left)
            if front < len(nodes):
                node.right = nodes[front]
                front += 1
                queue.append(node.right)
    return root

def merge_trees(t1, t2):
    """Merges two binary trees by summing values of overlapping nodes."""
    if not t1:
        return t2
    if not t2:
        return t1
    
    merged = TreeNode(t1.val + t2.val)
    merged.left = merge_trees(t1.left, t2.left)
    merged.right = merge_trees(t1.right, t2.right)
    return merged

def print_tree_level_order(root):
    """Prints the tree in a readable list format."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    # Clean up trailing nulls for cleaner output
    while result and result[-1] == "null":
        result.pop()
    return result

# --- User Input Execution ---
print("--- 1. Merge Two Binary Trees ---")
print("Enter tree nodes level by level (space-separated, use 'null' for empty nodes).")
input1 = input("Enter Tree 1 (e.g., 1 3 2 5): ").split()
input2 = input("Enter Tree 2 (e.g., 2 1 3 null 4 null 7): ").split()

tree1 = build_tree(input1)
tree2 = build_tree(input2)

merged_tree = merge_trees(tree1, tree2)
print("Merged Tree (Level Order):", print_tree_level_order(merged_tree))

#B 
