import numpy as np

db_size = 10
# data = np.random.permutation(db_size).tolist()
data = [6,2,5,45,3,1,4,56,8,7,9,0,15,48,3]

class Node(object):
    def __init__(self, lchild=None, rclild=None, elem=-1):
        self.lchild = lchild
        self.rchild = rclild
        self.elem = elem

def insert(root, elem):
    if root == None:
        root = Node(elem)
    else:
        if elem < root.elem:
            root.lchild = insert(root.lchild, elem)
        elif elem > root.elem:
            root.rchild = insert(root.rchild, elem)
        else:
            pass
    return root

# root = None
# for i, point in enumerate(data):
#     root = insert(root, point)
#
# print("a")


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
    return root

def inorderTraversal(root):
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None:
            continue
        if color == WHITE:
            stack.append((WHITE, node.rchild))
            stack.append((GRAY, node))
            stack.append((WHITE, node.lchild))
        else:
            res.append(node.elm)
    return res

root = None
for i, point in enumerate(data):
    root = insert(root, point)

print(inorderTraversal(root))