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
print("")

print("And this is the version of the stack-based queue with the")
print("expensive enqueue method.")
class Queue2:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []
        self.count = 0

    def enqueue2(self, data):
        if not self.stack_one:
            self.stack_one.append(data)
            self.count += 1
        else:
            while self.count > 0:
                self.stack_two.append(self.stack_one.pop())
                self.count -= 1
            self.stack_two.append(data)
            while self.stack_two:
                self.stack_one.append(self.stack_two.pop())
                self.count += 1
            

    def dequeue2(self):
        if self.stack_one:
            self.stack_one.pop()
            self.count -= 1
        else:
            return "queue is empty"

print("")
print("Here is the stack-based queue with the expensive enqueue.")
print("We check that the queue is empty.")
q = Queue2()
print(q.dequeue2())

print("")
print("We add elements to the queue.")
q.enqueue2("element1")
q.enqueue2("element2")
print("Now, we check our stack of elements.")
print(q.stack_one)
print("And we have how many elements?")
print(q.count)
print("")

print("Let's add one more element, element3; then let's")
print("remove two elements and make sure the only element")
print("remaining is the first element added.")

print("")
q.enqueue2("element3")
print("Here is the stack with the new element, element3.")
print(q.stack_one)
print("And here is the stack after two elements have been removed.")
q.dequeue2()
q.dequeue2()
print(q.stack_one)

print("")
print("And what is the count?")
print(q.count)


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
# Agarwal Chapter 5 Exercise 2
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
class Exercise2Node:
    def __init__(self, data):
        self.data = data
        self.nex = None
class Exercise2SinglyLinkedStack:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        node = Exercise2Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        node.nex = self.head
        self.head = node
    def delete(self):
        current = self.head
        while current.nex:
            if current.nex == self.tail:
                self.tail = current
                current.nex = None
                return
            current = current.nex
        self.head = None
        return
    def iter(self):
        current = self.head
        if current is None:
            print("List empty")
            return
        print(current.data)
        while current.nex:
            current = current.nex
            print(current.data)
print("---------------------------------")
print("Let's work with SinglyLinkedStack")
print("Let's add items and look at the list.")
number2 = Exercise2SinglyLinkedStack()
number2.append("one")
number2.append("two")
number2.append("three")
number2.append("four")
number2.iter()
print("This is the head {}".format(number2.head.data))
print("This is the tail {}".format(number2.tail.data))
print("Let's delete an item and look at the list.")
number2.delete()
number2.iter()


# 2nd attempt Agarwal array-based stack

overflow = 3
top = 0
stack = [0]*overflow
def push(data):
    global top
    if top < overflow:
        stack[top] = data
        top += 1
    else:
        print("stack overflow")
def pop():
    global top
    if top == 0:
        print("stack underflow")
    elif top == overflow:
        top -= 1
        stack[top] = 0
    else:
        top -= 1
        stack[top] = 0
def peek():
    if top == 0:
        print("list empty")
    else:
        print("The top element: {}".format(stack[top-1]))
def traverse():
    global top
    for i in range(overflow):
        print("position: {}".format(i))
        print(stack[i])

print("")
print("")
print("")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_*_*_*_*_*_*_*_*")
print("Let us push items to the stack until we experience overflow.")
print("Here is top: {}".format(top))
traverse()
print("****______****")
push("one")
print("Here is top: {}".format(top))
traverse()
print("We peek at the top element.")
peek()
print("////----****----____----****----////")
print("****______****")
push("two")
print("Here is top: {}".format(top))
traverse()
print("****______****")
push("three")
print("Here is top: {}".format(top))
traverse()
print("We peek at the top element.")
peek()
print("////----****----____----****----////")
print("****______****")
push("four")
print("////////////////////////////////////////////")
print("Let us pop items from the stack until we experience underflow.")
print("Here is top: {}".format(top))
traverse()
print("****______****")
pop()
print("Here is top: {}".format(top))
traverse()
print("We peek at the top element.")
peek()
print("////----****----____----****----////")
print("****______****")
pop()
print("Here is top: {}".format(top))
traverse()
print("We peek at the top element.")
peek()
print("////----****----____----****----////")
print("****______****")
pop()
print("Here is top: {}".format(top))
traverse()
print("****______****")
pop()
print("Here is top: {}".format(top))
traverse()
print("We peek at the top element.")
peek()
print("////----****----____----****----////")

# Second attempt, Agarwal's SinglyLinkedList Stack

class NodeStack011124:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedListStack011124:
    def __init__(self):
        self.top = None
        self.size = 0
    def peek_stack_011124(self):
        current = self.top
        print("This is in the stack:")
        while current:
            print(current.data)
            current = current.next
    def push_stack_011124(self, data):
        node = NodeStack011124(data)
        if self.top is None:
            self.top = node
            self.size += 1
        else:
            node.next = self.top
            self.top = node
            self.size += 1
    def pop_stack_011124(self):
        if self.top:
            current_top = self.top
            self.top = self.top.next
            self.size -= 1
            return current_top.data

print("")
single_stack = SinglyLinkedListStack011124()
print("size of the list: {}".format(single_stack.size))
print("We add an item to the list.")
single_stack.push_stack_011124("one")
single_stack.peek_stack_011124()
print("")
print("size of the list: {}".format(single_stack.size))
print("We add an item to the list.")
single_stack.push_stack_011124("two")
single_stack.peek_stack_011124()
print("")
print("size of the list: {}".format(single_stack.size))
print("We add an item to the list.")
single_stack.push_stack_011124("three")
single_stack.peek_stack_011124()
print("")
print("size of the list: {}".format(single_stack.size))
print("")
print("^-^-^-^")
print("We remove an item from the list.")
single_stack.pop_stack_011124()
print("size of the list: {}".format(single_stack.size))
single_stack.peek_stack_011124()
print("")
print("^-^-^-^")
print("We remove an item from the list.")
single_stack.pop_stack_011124()
print("size of the list: {}".format(single_stack.size))
single_stack.peek_stack_011124()
print("")
print("^-^-^-^")
print("We attempt to remove an item from the list.")
single_stack.pop_stack_011124()
print("size of the list: {}".format(single_stack.size))
single_stack.peek_stack_011124()
print("")
print("^-^-^-^")
print("We attempt to remove an item from the list.")
single_stack.pop_stack_011124()
print("size of the list: {}".format(single_stack.size))
single_stack.peek_stack_011124()

print("")
print("")
print("")
print("Bracket application of stacks")
def check_brackets011124(s):
    stack_of_brackets = SinglyLinkedListStack011124()
    last = ''
    for ch in s:
        if ch in ('{', '[', '('):
            stack_of_brackets.push_stack_011124(ch)
        if ch in ('}', ']', ')'):
            last = stack_of_brackets.pop_stack_011124()
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False
    if stack_of_brackets.size > 0:
        return False
    else:
        return True

test_strings = (
        "( 2**(-(x[i]-1)) - 2**(-x[i]) )",
        )
for s in test_strings:
    m = check_brackets011124(s)
    print("s: {}; verdict: {}".format(s, m))

print("")
print("")
print("")

# Second attempt at Agarwal's list-based queue
class ListQueue011724:
    def __init__(self):
        self.queue_data = []
        self.front = self.rear = 0
        self.size = 3
    def enqueue011724(self, data):
        if self.rear == self.size:
            print("Queue full; pop off an element.")
        else:
            self.queue_data.append(data)
            self.rear += 1
    def dequeue011724(self):
        if self.rear == self.front:
            print("Nothing in the queue.")
        else:
            self.queue_data.pop(0)
            self.rear -= 1
list_based_queue = ListQueue011724()
list_based_queue.enqueue011724("one")
list_based_queue.enqueue011724("two")
list_based_queue.enqueue011724("three")
list_based_queue.enqueue011724("four")
print("this is the rear: {}".format(list_based_queue.rear))
list_based_queue.dequeue011724()
list_based_queue.dequeue011724()
list_based_queue.dequeue011724()
list_based_queue.dequeue011724()
print("this is the rear: {}".format(list_based_queue.rear))


print("")
print("")
print("")

# Second attempt at Agarwal's LinkedList-based queue
class NodeQueue011824:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedListQueue011824:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None
    def enqueue011824(self, data):
        node = NodeQueue011824(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    def dequeue011824(self):
        if self.head is None:
            print("Queue is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
    def iterate011824(self):
        current = self.head
        if current is None:
            print("Nothing through which to iterate. The queue is empty.")
        while current:
            print(current.data)
            current = current.next
queue011824 = LinkedListQueue011824()
queue011824.dequeue011824()
queue011824.enqueue011824("one")
queue011824.iterate011824()
queue011824.dequeue011824()
queue011824.iterate011824()
queue011824.enqueue011824("two")
queue011824.iterate011824()
queue011824.dequeue011824()
queue011824.iterate011824()
queue011824.dequeue011824()
queue011824.enqueue011824(1)
queue011824.enqueue011824(2)
queue011824.enqueue011824(3)
queue011824.iterate011824()
queue011824.dequeue011824()
queue011824.iterate011824()
queue011824.dequeue011824()
queue011824.iterate011824()
queue011824.dequeue011824()
queue011824.iterate011824()
queue011824.dequeue011824()
