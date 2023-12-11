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
class NodePreOrder:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0_pre = NodePreOrder("root")

n1_pre = NodePreOrder("left")
n0_pre.left_child = n1_pre

n2_pre = NodePreOrder("right")
n0_pre.right_child = n2_pre

n3_pre = NodePreOrder("left_0")
n1_pre.left_child = n3_pre

n4_pre = NodePreOrder("left_1")
n1_pre.right_child = n4_pre

n5_pre = NodePreOrder("right_0")
n2_pre.left_child = n5_pre

n6_pre = NodePreOrder("right_1")
n2_pre.right_child = n6_pre

n7_pre = NodePreOrder("left_0_1")
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
class NodeInOrder:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0_in = NodeInOrder("root")

n1_in = NodeInOrder("left")
n0_in.left_child = n1_in

n2_in = NodeInOrder("right")
n0_in.right_child = n2_in

n3_in = NodeInOrder("left_0")
n1_in.left_child = n3_in

n4_in = NodeInOrder("left_1")
n1_in.right_child = n4_in

n5_in = NodeInOrder("right_0")
n2_in.left_child = n5_in

n6_in = NodeInOrder("right_0_0")
n5_in.left_child = n6_in

n7_in = NodeInOrder("right_0_1")
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
class NodePostOrder:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n0_post = NodePostOrder("root")

n1_post = NodePostOrder("left")
n0_post.left_child = n1_post

n2_post = NodePostOrder("right")
n0_post.right_child = n2_post

n3_post = NodePostOrder("left_0")
n1_post.left_child = n3_post

n4_post = NodePostOrder("left_1")
n1_post.right_child = n4_post

n5_post = NodePostOrder("left_1_0")
n4_post.left_child = n5_post

n6_post = NodePostOrder("left_1_1")
n4_post.right_child = n6_post

n7_post = NodePostOrder("right_0")
n2_post.left_child = n7_post

n8_post = NodePostOrder("right_1")
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

# Binary tree level-order
# We first recall the list-based queue
class ListQueue:
    def __init__(self):
        self.items = []
        self.front = 0
        self.rear = 0
        self.size = 4

    def enqueue(self, data):
        if self.size == self.rear:
            print("queue full")
        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("queue is empty")
        else:
            data = self.items.pop(0)
            self.rear -= 1
            return data
print("We revisit the list-based queue.")
print("This is the expected order of appearance:")
the_queue = ListQueue()
the_queue.enqueue("root")
print("The root node: {}".format(the_queue.dequeue()))
the_queue.enqueue("left")
the_queue.enqueue("right")
print("The left child of root: {}".format(the_queue.dequeue()))
the_queue.enqueue("left_0")
the_queue.enqueue("left_1")
print("The right child of root: {}".format(the_queue.dequeue()))
the_queue.enqueue("right_0")
the_queue.enqueue("right_1")
print("The left child of left: {}".format(the_queue.dequeue()))
print("The right child of left: {}".format(the_queue.dequeue()))
print("The left child of right: {}".format(the_queue.dequeue()))
print("The right child of right: {}".format(the_queue.dequeue()))
print("")
print("Let's try this out:")

class NodeLevel:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# Here is the level-order traverse link
n1_level = NodeLevel("root")

n2_level = NodeLevel("left")
n1_level.left_child = n2_level

n3_level = NodeLevel("right")
n1_level.right_child = n3_level

n4_level = NodeLevel("left_0")
n2_level.left_child = n4_level

n5_level = NodeLevel("left_1")
n2_level.right_child = n5_level

n6_level = NodeLevel("right_0")
n3_level.left_child = n6_level

n7_level = NodeLevel("right_1")
n3_level.right_child = n7_level

def level_order_traverse(root):
    nodes_popped = []
    nodes_in_queue = [root]
    while len(nodes_in_queue) > 0:
        node = nodes_in_queue.pop(0)
        nodes_popped.append(node.data)
        if node.left_child:
            nodes_in_queue.append(node.left_child)
        if node.right_child:
            nodes_in_queue.append(node.right_child)
    return nodes_popped
print(level_order_traverse(n1_level))
print("")

# Expression tree
print("Here is the Expression Tree result")
class TreeNodeExpression:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class StackExpression:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        popped_item = self.items.pop()
        return popped_item

stack = StackExpression()

expression = "3 5 + 4 5 - *".split()
for term in expression:
    if term in "+-*/":
        node = TreeNodeExpression(term)
        node.right = stack.dequeue()
        node.left = stack.dequeue()
    else:
        node = TreeNodeExpression(int(term))
    stack.enqueue(node)

def calculate(node_item):
    if node_item.data == "+":
        return calculate(node_item.left) + calculate(node_item.right)
    elif node_item.data == "-":
        return calculate(node_item.left) - calculate(node_item.right)
    elif node_item.data == "*":
        return calculate(node_item.left) * calculate(node_item.right)
    elif node_item.data == "/":
        return calculate(node_item.left) / calculate(node_item.right)
    else:
        return node_item.data

print(calculate(stack.dequeue()))
print("")

# Binary Search Tree

print("Here is out Binary Search Tree")

class NodeSearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class SearchTree:
    def __init__(self):
        self.root = None
    def onboarding(self, data):
        node = NodeSearchTree(data)
        if self.root is None:
            self.root = node
            return self.root
        else:
            current = self.root
            parent = None
            while current:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return 
                else:
                    current = current.right
                    if current is None:
                        parent.right = none
                        return

n0_search_tree = NodeSearchTree("root")

n1_search_tree = NodeSearchTree("left")
n0_search_tree.left = n1_search_tree

n2_search_tree = NodeSearchTree("right")
n0_search_tree.right = n2_search_tree

n3_search_tree = NodeSearchTree("left_0")
n1_search_tree.left = n3_search_tree

n4_search_tree = NodeSearchTree("left_0_0")
n3_search_tree.left = n4_search_tree

n5_search_tree = NodeSearchTree("left_0_1")
n3_search_tree.right = n5_search_tree

def in_order_traverse_search_tree(node):
    if node is None:
        return
    if node.left:
        in_order_traverse_search_tree(node.left)
    print(node.data)
    if node.right:
        in_order_traverse_search_tree(node.right)

in_order_traverse_search_tree(n0_search_tree)
print("")
