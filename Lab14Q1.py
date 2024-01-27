'''Q1: Implement an algorithm to find the minimum and maximum values stored in a BST.'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min(node):
    # Traverse the left subtree until the leftmost node is reached
    while node.left is not None:
        node = node.left
    return node.value

def find_max(node):
    # Traverse the right subtree until the rightmost node is reached
    while node.right is not None:
        node = node.right
    return node.value

# Example usage:
# Assuming you have a BST rooted at 'root'
# You can create the tree and call the functions like this:

# Sample BST:
#         10
#        /  \
#       5   15
#      / \    \
#     3   7   18

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Find the minimum and maximum values
min_value = find_min(root)
max_value = find_max(root)

print("Minimum value in the BST:", min_value)
print("Maximum value in the BST:", max_value)
