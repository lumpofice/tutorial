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

print("")

# Binary tree pre-order traverse
class Node_pre_order:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0 = Node_pre_order("root")

n1 = Node_pre_order("left")
n0.left_child = n1

n2 = Node_pre_order("right")
n0.right_child = n2

n3 = Node_pre_order("left_0")
n1.left_child = n3

n4 = Node_pre_order("left_1")
n1.right_child = n4

n5 = Node_pre_order("right_0")
n2.left_child = n5

n6 = Node_pre_order("right_1")
n2.right_child = n6

n7 = Node_pre_order("left_0_1")
n3.right_child = n7

print("Printing pre-order nodes:")

def pre_order_traverse(node):
    current = node
    if current is None:
        return
    print(current.data)
    pre_order_traverse(current.left_child)
    pre_order_traverse(current.right_child)
pre_order_traverse(n0)

print("")

# Binary tree in-order traverse
class Node_in_order:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0 = Node_in_order("root")

n1 = Node_in_order("left")
n0.left_child = n1

n2 = Node_in_order("right")
n0.right_child = n2

n3 = Node_in_order("left_0")
n1.left_child = n3

n4 = Node_in_order("left_1")
n1.right_child = n4

n5 = Node_in_order("right_0")
n2.left_child = n5

n6 = Node_in_order("right_0_0")
n5.left_child = n6

n7 = Node_in_order("right_0_1")
n5.right_child = n7

print("Printing in-order nodes:")

def in_order_traverse(node):
    current = node
    if current is None:
        return
    in_order_traverse(current.left_child)
    print(current.data)
    in_order_traverse(current.right_child)
in_order_traverse(n0)

print("")
