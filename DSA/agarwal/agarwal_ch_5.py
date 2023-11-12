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
