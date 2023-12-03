# Binary Tree
# ----------------------------
# ----------------------------
# ----------------------------
print("")
print("Let's work with Binary Trees")
print("")
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# left is the left child of root
# right is the right child of root
# left_0 is the left child of left
# left_0_1 is the right child of left_0
n1 = Node("root")

n2 = Node("left")
n1.left_child = n2

n3 = Node("right")
n1.right_child = n3

n4 = Node("left_0")
n2.left_child = n4

n5 = Node("right_1")
n3.right_child = n5

n6 = Node("left_0_1")
n4.right_child = n6

current = n1
while current:
    print(current.data)
    current = current.left_child


# Binary tree in-order traverse
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0 = Node("root")

n1 = Node("left")
n0.left_child = n1

n2 = Node("right")
n0.right_child = n2

n3 = Node("left_0")
n1.left_child = n3

n4 = Node("left_1")
n1.right_child = n4

n5 = Node("right_0")
n2.left_child = n5

n6 = Node("right_1")
n2.right_child = n6

n7 = Node("left_0_1")
n3.right_child = n7

print("")
print("Let's work with in-order traversals of Binary Trees")
print("")

def in_order_traverse(node):
    current = node
    if current is None:
        return
    print(current.data)
    in_order_traverse(current.left_child)
    in_order_traverse(current.right_child)
in_order_traverse(n0)
