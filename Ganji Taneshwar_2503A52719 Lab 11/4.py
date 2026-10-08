class BST:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def insert(self, root, value):
        if root is None:
            return self.Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.value]
            + self.inorder_traversal(root.right)
        )

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def inorder(self):
        return self.inorder_traversal(self.root)

# Example usage:
if __name__ == "__main__":
    bst = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for value in values_to_insert:
        bst.insert_value(value)

    print("Inorder Traversal of the BST:", bst.inorder())
    
                                                         