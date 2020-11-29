import numpy as np

db_size = 10
# data = np.random.permutation(db_size).tolist()
data = [6,2,5,3,1,4,8,7,9,0]

class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value


def insert(root, key, value=-1):
    if root is None:
        root = Node(key, value)

    else:
        if key < root.key:
            root.left = insert(root.left, key, value)
        elif key > root.key:
            root.right = insert(root.right, key, value)
        else:
            pass
    return root

root = None
print(data)
for i, point in enumerate(data):
    root = insert(root, point, i)
    # print(point)

def search_recursive(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search_recursive(root.left, key)
    elif key > root.key:
        return search_recursive(root.right, key)

def search_iterative(root, key):
    current_node = root
    while current_node is not None:
        if current_node.key == key:
            return current_node
        elif key < current_node.key:
            current_node =  current_node.left
        elif key > current_node.key:
            # key > current_node.key
            current_node = current_node.right

# print(search_iterative(root, 4))
# print(search_recursive(root, 4))

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
    return root


#
# print(div([1,2,3,4,5,5,6,6,7,7], 6))
inorder(root)