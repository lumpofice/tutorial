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

n0_pre = Node_pre_order("root")

n1_pre = Node_pre_order("left")
n0_pre.left_child = n1_pre

n2_pre = Node_pre_order("right")
n0_pre.right_child = n2_pre

n3_pre = Node_pre_order("left_0")
n1_pre.left_child = n3_pre

n4_pre = Node_pre_order("left_1")
n1_pre.right_child = n4_pre

n5_pre = Node_pre_order("right_0")
n2_pre.left_child = n5_pre

n6_pre = Node_pre_order("right_1")
n2_pre.right_child = n6_pre

n7_pre = Node_pre_order("left_0_1")
n3_pre.right_child = n7_pre

print("Printing pre-order nodes:")

def pre_order_traverse(node):
    current = node
    if current is None:
        return
    print(current.data)
    pre_order_traverse(current.left_child)
    pre_order_traverse(current.right_child)
pre_order_traverse(n0_pre)

print("")

# Binary tree in-order traverse
class Node_in_order:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0_in = Node_in_order("root")

n1_in = Node_in_order("left")
n0_in.left_child = n1_in

n2_in = Node_in_order("right")
n0_in.right_child = n2_in

n3_in = Node_in_order("left_0")
n1_in.left_child = n3_in

n4_in = Node_in_order("left_1")
n1_in.right_child = n4_in

n5_in = Node_in_order("right_0")
n2_in.left_child = n5_in

n6_in = Node_in_order("right_0_0")
n5_in.left_child = n6_in

n7_in = Node_in_order("right_0_1")
n5_in.right_child = n7_in

print("Printing in-order nodes:")

def in_order_traverse(node):
    current = node
    if current is None:
        return
    in_order_traverse(current.left_child)
    print(current.data)
    in_order_traverse(current.right_child)
in_order_traverse(n0_in)

print("")


# Binary tree post-order
class Node_post_order:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0_post = Node_post_order("root")

n1_post = Node_post_order("left")
n0_post.left_child = n1_post

n2_post = Node_post_order("right")
n0_post.right_child = n2_post

n3_post = Node_post_order("left_0")
n1_post.left_child = n3_post

n4_post = Node_post_order("left_1")
n1_post.right_child = n4_post

n5_post = Node_post_order("left_1_0")
n4_post.left_child = n5_post

n6_post = Node_post_order("left_1_1")
n4_post.right_child = n6_post

n7_post = Node_post_order("right_0")
n2_post.left_child = n7_post

n8_post = Node_post_order("right_1")
n2_post.right_child = n8_post

print("Printint post-order nodes:")

def post_order_traverse(node):
    current = node
    if current is None:
        return
    post_order_traverse(current.left_child)
    post_order_traverse(current.right_child)
    print(current.data)
post_order_traverse(n0_post)

print("")
