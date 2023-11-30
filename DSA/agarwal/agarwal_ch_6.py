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

