class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # probably balance factor

class AVLTree:
    def insert(self, root, key):
        pass

    def left_rotate(self, z):
        pass

    def right_rotate(self, z):
        pass

    def get_height(self, root):
        pass

    def get_balance(self, root):
        pass

    def pre_order(self, root):
        pass


# Driver program to test above function
myTree = AVL_Tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""

# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")

myTree.preOrder(root)
