class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # probably balance factor

class AVLTree:
    def insert(self, root, key):
        # normal BST search tree
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # update the height of the tree
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.left))
        balance = self.get_balance(root)

        # Todo if balance is higher or less than 1 then rotate

        # Left left?
        if balance > 1 and key < root.left.val:
            pass

        # right right ?
        if balance < -1 and key > root.right.val:
            pass

        # left right
        if balance > 1 and key > root.left.val:
            pass

        # right left
        if balance < -1 and key < root.right.val:
            pass

    def left_rotate(self, z):
        pass

    def right_rotate(self, z):
        pass

    def get_height(self, root):
        if root is None:
            return 0

        return root.height

    def get_balance(self, root):
        if root is None:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

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
