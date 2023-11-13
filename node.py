
# AVL node class
class AVLNode:

    # AVL node class constructor
    def __init__(self, data, choice):
        self.data = data
        self.choice = choice
        self.left = None
        self.right = None
        self.height = 1

# AVL class that handles all my implementations for my balanced tree
class AVL:
    # AVL default constructor
    def __init__(self):
        self.root = None


    # Insert wrapper function
    def insert(self, data, choice):
        self.root = self._insert(self.root, data, choice)

    # Insert function that inserts like a normal BST, and rotates when it needs to 
    def _insert(self, node, data, choice):
        if not node:
            return AVLNode(data, choice)
        
        if data < node.data:
            node.left = self._insert(node.left, data, choice)
        else:
            node.right = self._insert(node.right, data, choice)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1:
            if data < node.left.data:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if data > node.right.data:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    # Rotate left function that handles the cases when the tree needs to rotate left
    def _rotate_left(self, node):
        new_node = node.right
        temp = new_node.left

        new_node.left = node 
        node.right = temp 

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_node.height = 1 + max(self._get_height(node.left), self._get_height(new_node.right))

        return new_node

    # Rotate right function that handles the cases when the tree needs to rotate right 
    def _rotate_right(self, node):
        new_node = node.left
        temp = new_node.right

        new_node.right = node
        node.left = temp 

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_node.height = 1 + max(self._get_height(new_node.left), self._get_height(new_node.right))

        return new_node

    # Get function that returns the height of the node that was passed into it 
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get balance that returns the balance of the node that was passed into it 
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Retrieve wrapper function
    def retrieve(self, data):
        return self._retrieve(self.root, data)

    # Retrieve recursive function that returns None if unsuccessful
    def _retrieve(self, node, data):
        if not node:
            return None

        if data == node.data:
            return node.data
        elif data < node.data:
            return self._retrieve(node.left, data)
        else:
            return self._retrieve(node.right, data)

    # Display wrapper function
    def display(self):
        self._display(self.root)

    # Display recursive function that returns all the data of the tree 
    def _display(self, node):
        if node:
            self._display(node.left)
            print('-' * 100)
            print("Your username is: ", node.data)
            node.choice.print()
            self._display(node.right)
