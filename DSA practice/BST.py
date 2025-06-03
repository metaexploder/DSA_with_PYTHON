class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_balanced_bst(sorted_array, start, end):
    """ Recursively builds a balanced BST from a sorted array. """
    if start > end:
        return None

    # Select the middle element as the root
    mid = (start + end) // 2
    root = Node(sorted_array[mid])

    # Recursively build left and right subtrees
    root.left = build_balanced_bst(sorted_array, start, mid - 1)
    root.right = build_balanced_bst(sorted_array, mid + 1, end)

    return root

def print_tree(node, level=0, prefix="Root: "):
    """ Prints the actual BST structure in a readable format. """
    if node:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Given elements
elements = [3, 5, 7, 10, 15, 20, 30]
elements.sort()  # Ensure the list is sorted before building BST

# Build balanced BST
root = build_balanced_bst(elements, 0, len(elements) - 1)

# Print actual BST structure
print("\nBalanced Binary Search Tree Structure:")
print_tree(root)