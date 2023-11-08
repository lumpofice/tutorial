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
