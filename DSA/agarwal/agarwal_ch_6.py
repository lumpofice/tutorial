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
print("-----------------")
print("Here, we work with a binary search tree")
print("")

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return parent.left_child 
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return parent.right_child

    def inorder(self, root_node): 
        current = root_node 
        if current is None: 
            return 
        self.inorder(current.left_child) 
        print(current.data) 
        self.inorder(current.right_child)
        
                    
    def get_node_with_parent(self, data): 
        parent = None 
        current = self.root_node 
        if current is None: 
            return (parent, None) 
        while True: 
            if current.data == data: 
                return (parent, current) 
            elif current.data > data: 
                parent = current 
                current = current.left_child 
            else: 
                parent = current 
                current = current.right_child 
        return (parent, current) 
   

    def remove(self, data):  
        parent, node = self.get_node_with_parent(data)  
 
        if parent is None and node is None:  
            return False  
 
        # Get children count  
        children_count = 0  
 
        if node.left_child and node.right_child:  
            children_count = 2  
        elif (node.left_child is None) and (node.right_child is None):  
            children_count = 0  
        else:  
            children_count = 1  
        
        if children_count == 0:  
            if parent:  
                if parent.right_child is node:  
                    parent.right_child = None  
                else:  
                    parent.left_child = None  
            else:  
                self.root_node = None 
        elif children_count == 1:  
            next_node = None  
            if node.left_child:  
                next_node = node.left_child  
            else:  
                next_node = node.right_child  
 
            if parent:  
                if parent.left_child is node:  
                    parent.left_child = next_node  
                else:  
                    parent.right_child = next_node  
            else:  
                self.root_node = next_node  
        else:  
            parent_of_leftmost_node = node 
            leftmost_node = node.right_child 
            while leftmost_node.left_child:  
                parent_of_leftmost_node = leftmost_node 
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
    
            if parent_of_leftmost_node.left_child == leftmost_node:  
                parent_of_leftmost_node.left_child = leftmost_node.right_child  
            else:  
                parent_of_leftmost_node.right_child = leftmost_node.right_child 
            
            
    
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

                
tree = Tree()
n0 = tree.insert(5)
print("node")
print(n0.data)
n1 = tree.insert(2)
print("left child")
print(n0.left_child.data)
n2 = tree.insert(7)
print("right child")
print(n0.right_child.data)
n3 = tree.insert(10)
print("right child 1")
print(n2.right_child.data)
n4 = tree.insert(1)
print("left child 0")
print(n1.left_child.data)
n5 = tree.insert(6)
print("right child 0")
print(n2.left_child.data)
n6 = tree.insert(8)
print("right child 1 0")
print(n3.left_child.data)
n7 = tree.insert(11)
print("right child 1 1")
print(n3.right_child.data)
n8 = tree.insert(9)
print("right child 1 0 1")
print(n6.right_child.data)

print("")
print("Here is the tree, from left-most node to right-most node")
tree.inorder(n0)

print("")
print("let's search for {}".format(n2.data))
tree.search(7)      

print("")
print("let's traverse the tree with root node {}".format(n3.data))
tree.inorder(n3)

print("")
print("let's remove {}".format(n2.data))
tree.remove(7)
print("okay, now let's search for it again")
tree.search(7)

print("")
print("let's traverse the tree once more")
tree.inorder(n0)

print("")
print("let's traverse the tree with root node {} once more".format(n3.data))
tree.inorder(n3)


# Second attempt at the Agarwal in-order traverse of Binary Tree algorithm
print("")
print("")
print("second attempt at in-order traverse of binary tree")
print("--------------------------------")
class BinaryTreeNode012324:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
n_0 = BinaryTreeNode012324("root")

n_1 = BinaryTreeNode012324("left")
n_0.left = n_1

n_2 = BinaryTreeNode012324("right")
n_0.right = n_2

n_3 = BinaryTreeNode012324("left_0")
n_1.left = n_3

n_4 = BinaryTreeNode012324("left_1")
n_1.right = n_4

n_5 = BinaryTreeNode012324("right_1")
n_2.right = n_5

n_6 = BinaryTreeNode012324("left_0_0")
n_3.left = n_6

n_7 = BinaryTreeNode012324("left_0_1")
n_3.right = n_7

def in_order_traverse012324(root):
    current = root
    if current.left:
        in_order_traverse012324(current.left)
    print(current.data)
    if current.right:
        in_order_traverse012324(current.right)

in_order_traverse012324(n_0)

print("")
print("")
print("second attempt at Pre-Order")
def pre_order_traverse012324(root):
    if root:
        print(root.data)
    if root.left:
        pre_order_traverse012324(root.left)
    if root.right:
        pre_order_traverse012324(root.right)
    return

pre_order_traverse012324(n_0)

print("")
print("")
print("second attempt at Post-Order")
def post_order_traverse012324(root):
    if root is None:
        return
    post_order_traverse012324(root.left)
    post_order_traverse012324(root.right)
    print(root.data)

post_order_traverse012324(n_0)

print("")
print("")
print("")
print("Second attempt at the binary tree level traverse algorithm.")
class ListBasedBinaryTreeQueue012324:
    def __init__(self):
        self.items1 = []
        self.items2 = []
    def enqueue012324(self, node):
        self.items1.append(node)
    def dequeue012324(self):
        while self.items1:
            self.items2.append(self.items1.pop())
        if self.items2:
            first = self.items2.pop()
            while self.items2:
                self.items1.append(self.items2.pop())
            return first
        return "queue is empty"

queue012324 = ListBasedBinaryTreeQueue012324()
def level_traverse012324(root):
    global queue012324
    queue012324.enqueue012324(root)
    while queue012324.items1:
        the_pop = queue012324.dequeue012324()
        print(the_pop.data)
        if the_pop.left:
            queue012324.enqueue012324(the_pop.left)
        if the_pop.right:
                queue012324.enqueue012324(the_pop.right)

level_traverse012324(n_0)


# Second attempt at Expression Trees 02_09_24
print("")
print("")
print("")
print("")
print("Expression Tree 02_09_24")
print("------------------------------------")
class TreeNode020924:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class ExpressionStack020924:
    def __init__(self):
        self.items = []
    def append020924(self, node):
        self.items.append(node)
    def pop020924(self):
        return self.items.pop()
expression020924 = "3 4 + 8 5 - *".split()
stack020924 = ExpressionStack020924()
for item in expression020924:
    if item in "+-*/":
        node = TreeNode020924(item)
        node.left = stack020924.pop020924()
        node.right = stack020924.pop020924()
        stack020924.append020924(node)
    else:
        stack020924.append020924(TreeNode020924(int(item)))
def calc020924(root):
    if root.data == "+":
        return calc020924(root.left) + calc020924(root.right)
    elif root.data == "-":
        return calc020924(root.left) - calc020924(root.right)
    elif root.data == "*":
        return calc020924(root.left)*calc020924(root.right)
    elif root.data == "/":
        return calc020924(root.left)/calc020924(root.right)
    else:
        return root.data
root020924 = stack020924.pop020924()
result020924 = calc020924(root020924)
print("Mathematical Result: {}".format(result020924))

# Second attempt at Binary Search Trees insert method 02_12_24
print("")
print("")
print("")
print("")
print("Binary Search Tree insert method 02_12_24")
print("------------------------------------")
class Node021224:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree021224:
    def __init__(self):
        self.root = None
    def insert(self, data):
        node = Node021224(data)
        if self.root is None:
            self.root = node
        else:
            if node.data < self.root.data:
                current = self.root
                while node.data < current.data:
                    if current.left is None:
                        current.left = node
                    else:
                        current = current.left
            else:
                current = self.root
                while node.data > current.data:
                    if current.right is None:
                        current.right = node
                    else:
                        current = current.right
    def in_order(self, root):
        if root.left:
            self.in_order(root.left)
        print(root.data)
        if root.right:
            self.in_order(root.right)
        return
tree = Tree021224()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(8)
tree.in_order(tree.root)
