# Stack in an array
# ------------------
# ------------------
# ------------------
size = 3
data = ["a"]*(size)   #Initialize the stack

top = -1
print("{} is the initial stack".format(data[0 : top+1]))

print("")

stop_overflow = "Stack Overflow"
stop_underflow = "Stack Underflow"

def push(x):
  global top
  global stop_overflow
  if top >= size-1:
    return stop_overflow
  else:
    top += 1
    data[top] = x
   
def pop():
    global top
    global stop_underflow
    if top == -1:
        return stop_underflow
    else:
        data[top] = "a"
        top -= 1
   
print("Now, we push")
print("")

n = 5
for i in range(n):
    if push(i) == stop_overflow:
        print("We reached {}".format(push(i)))
        break
    else:
        print("{} is the updated data".format(data[0 : top+1]))
       
print("")
print("{} Here is the full stack".format(data[0 : top+1]))
print("")

print("Now, we pop")
print("")

for i in range(n):
    if pop() == stop_underflow:
        print("We reached {}".format(stop_underflow))
        break
    else:
        print("{} is the updated data".format(data[0 : top+1]))
       
print(data[0 : top+1])





# Stack in a linked list
# ----------------------
# ----------------------
# ----------------------
# ----------------------
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            if self.top.next:
                self.top = self.top.next
                self.size -= 1
                return data
            else:
                self.top = None
                self.size -= 1
                return "{}, leaving the stack empty,".format(data)
        else:
            return "Stack is empty"

words = Stack()
words.push("egg")
words.push("ham")
words.push("spam")

print("Let's begin by adding elements to the stack.")
print("--------------------------------------------")
print("--------------------------------------------")
print("--------------------------------------------")
print("")

print("Now, let's list out the elements in the stack.")
current = words.top
while current:
    print("{} is our node data in the initial stack.".format(current.data))
    current = current.next
   
print("")

print("Now, let's pop one of the elements off of the stack.")    
print("{} just got popped".format(words.pop()))

print("")

print("Let's take stock of what we have remaining in the stack.")
current = words.top
while current:
    print("{} is our node data in the updated stack.".format(current.data))
    current = current.next
   
print("")

print("Now, let's pop the remaining elements until our stack is empty.")
print("{} just got popped".format(words.pop()))
print("{} just got popped".format(words.pop()))
print("{}".format(words.pop()))
print("")


# Checking bracket opening and closing matches with the linked list stack
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def check_brackets(expression):
    brackets_stack = Stack()
    for ch in expression:
        if ch in ('{', '[', '('):
            brackets_stack.push(ch)
        if ch in ('}', ']', ')'):
            last = brackets_stack.pop()
            if (
                    (last == '{, leaving the stack empty,' or last == '{') 
                    and ch == '}'
                ):
                continue
            elif (
                    (last == '[, leaving the stack empty,' or last == '[') 
                    and ch == ']'
                ):
                continue
            elif (
                    (last == '(, leaving the stack empty,' or last == '(') 
                    and ch == ')'
                ):
                continue
            else:
                return False
    if brackets_stack.size > 0:
        return False
    else: 
        return True

s1 = (
        "{foo}",
        "[]",
        "()",
        "{}",
        "{[]}",
        "{([])}",
        "((()))"
)

for s in s1:
    m = check_brackets(s)
    print("{}: {}".format(s, m))
print("")



# List-based queue
# ----------------
# ----------------
# ----------------
class ListQueue:
    def __init__(self):
        self.front = self.rear = 0
        self.items = []
        self.size = 3

    def enqueue(self, data):
        if self.rear == self.size:
            print("Queue is full")
        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            data = self.items.pop(0)
            self.size -= 1
            self.rear -= 1
            return data

print("Let's add elements to the array-based queue.")
the_queue = ListQueue()
the_queue.enqueue("first")
the_queue.enqueue("second")
the_queue.enqueue("third")
the_queue.enqueue("fourth")
print("")
print("Here are the items in the array-based queue:")
print(the_queue.items)
print("")
print("What is the size of our array-based queue?")
print(the_queue.size)
print("")

print("Let's remove some items, then check the size.")
the_queue.dequeue()
the_queue.dequeue()
the_queue.dequeue()
print("We have removed some items. Here is the new size:")
print(the_queue.size)
print("")

print("Let's try removing one more item.")
the_queue.dequeue()
print("")


# Linked list queue
# ----------------
# ----------------
# ----------------
class Node:
    def __init__(self, data=None, nex=None, prev=None):
        self.data = data
        self.nex = nex
        self.prev = prev

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new = Node(data, None, None)
        if self.head == None:
            self.head = new
            self.tail = self.head
        else:
            new.prev = self.tail
            self.tail.nex = new
            self.tail = new
        self.size += 1

    def dequeue(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        elif self.size > 1:
            self.head = self.head.nex
            self.head.prev = None
            self.size -= 1
        elif self.size < 1:
            return "Queue is empty"

print("Let's add elements to the linked list based queue")
queue = Queue()
queue.enqueue("gain")
queue.enqueue("function")
queue.enqueue("loss")
print("")

print("We have added items to the queue. Let's check the size.")
print(queue.size)
print("")

print("Now, let's remove an item from the linked list queue.")
queue.dequeue()
print("")

print("An item has been removed from the linked list queue.")
print("Let's check the new size.")
print(queue.size)
print("")


# Stack based queue
# -----------------------------
# -----------------------------
# -----------------------------
print("Recall that we want to remove elements from the")
print("front of the list. So, we invert stack_1, which becomes")
print("stack_2, from which we remove the 'tail' element.")
print("")

print("This is the stack-based queue that has an expensive dequeue method.")
print("")

class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, data):
        self.stack_1.append(data)

    def dequeue(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        if not self.stack_2:
            return "stack_2 is empty"
        return self.stack_2.pop()

print("We add some elements to the stack based queue.")
queue = Queue()
queue.enqueue("staple")
queue.enqueue("clip")
queue.enqueue("paper")
print("")

print("Let's look at stack_1")
print(queue.stack_1)
print("")

print("Let's pop off some of the elements.")
print("We pop the element {}".format(queue.dequeue()))
print("Now, stack_1 is: {}".format(queue.stack_1))
print("and stack_2 is: {}".format(queue.stack_2))
print("Next, we pop off the element {}".format(queue.dequeue()))
print("giving us stack_1: {}".format(queue.stack_1))
print("and stack_2: {}".format(queue.stack_2))
