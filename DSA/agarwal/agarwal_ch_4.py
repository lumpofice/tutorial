# My version of Agarwal's Singly Linked List

class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

       
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0
       
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def append_at_a_location(self, data, index):  
        current = self.head
        prev = self.head
        node = Node(data)
        count = 0
        while current:
            if index == 0:
                node.next = current
                self.head = node
                self.size += 1
                return
            if count < index:  
                prev = current
                if current.next is None:
                    current.next = node
                    self.size += 1
                    return
                current = current.next
                count += 1
            elif count == index:
                node.next = current  
                prev.next = node
                count += 1
            else:
                prev = current
                current = current.next
                count += 1
        self.size += 1
        return  

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
   
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
   
    def search(self, data):
        for node in self.iter():
            if data == node:
                print("Yes. This node exists in this list.")
                return
        print("No. That node does not exist in this list.")
               
           
print("Let's begin the output of the SinglyLinkedList:")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print(" ")
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append("jam")
words.append("clam")
words.append("fan")

print("After the list is initialized, we have:")
current = words.head
while current:
    print(current.data)
    current = current.next
print(" ")
   
   
print("How large is the list?")
print(words.size)
print(" ")

words.append_at_a_location('new', 0)


print("Here, we check the list after inserting a new node. We now have:")
current = words.head
while current:
    print(current.data)
    current = current.next
print(" ")

print("Does 'sspam' exist in the list?")
words.search('sspam')
print(" ")

print("Does 'spam' exist in the list?")
words.search('spam')
print(" ")

print("How large is the list, now?")
print(words.size)
print(" ")


print("We can delete any node.")
words.delete("fan")
print(" ")

print("Here is the updated list:")
current = words.head
while current:
    print(current.data)
    current = current.next
print(" ")


print("How many objects are in our list now?")
print(words.size)
print(" ")


# My version of Agarwal's Doubly Linked List

class Node:
    def __init__ (self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
       
class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.count = 0
       
    def append(self, data):
        #Append an item at the end of the list.  
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
       
    def append_at_start(self, data):
        # Append an item at beginning to the list.
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
       
    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        new_node = Node(data, None, None)
        counter = 0
        while current:
            if counter == index:
                if counter == 0:
                    new_node.prev = None
                    new_node.next = prev
                    self.head = new_node
                    self.count += 1
                    return
                else:
                    new_node.prev = prev
                    new_node.next = current
                    prev.next = new_node
                    current.prev = new_node
                    self.count += 1
                    return
            prev = current
            current = current.next
            if current is None:
                new_node.prev = prev
                new_node.next = current
                prev.next = new_node
                self.count += 1
                return
            counter += 1

    def delete(self, data):
        # Delete a node from the list.
        current = self.head
        node_deleted = False
        if current is None:       #List is empty
            print("List is empty")
        elif current.data == data:   #Item found at starting of list
            self.head.prev = None
            node_deleted = True
            print(data, " item deleted")
            self.head = current.next

        elif self.tail.data == data:   #Item found at the end of list.
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
            print(data, " item deleted")

        else:
            while current:          #search and delete 
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                    print(data, " item deleted")
                current = current.next
            if node_deleted == False:   #Item not found
                print("Item not found")
        if node_deleted:
            self.count -= 1
    
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print("Our quarry exists!")
                return
        print("Wild goose chase!")
        return


print("Let's begin the output of the DoublyLinkedList:")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print(" ")

words = DoublyLinkedList()
print("We have initiated the class. How many items in our list?")
print(words.count)
print(" ")

words.append("egg")
words.append("ham")
print("We have appended two items to the list. List count is now:")
print(words.count)
print(" ")

words.append_at_start('book')
print("We have appended an item at the start of the list. List count:")
print(words.count)
print(" ")

words.append("eggs")
words.append("hams")

words.append_at_a_location('hammy', 5)

print("We have appended two more items using the append method."\
        " We have also appended at an arbitrary location within the list."\
        " The number of objects in our list now:")
print(words.count)
print(" ")

print("Here is our list.")
current = words.head
while current:
    print(current.data)
    current = current.next
print(" ")

print("Now, we search for items in the list.")
print("Does this item belong to the list?")
words.contains("ham")
print("Does this item?")
words.contains("hamburger")
print(" ")

print("Now, we delete some items.")
print("Let's attempt to delete an item.")
print("Was deletion successful?")
words.delete("ham")
print(" ")

print("Here is our list count:")
print(words.count)
print(" ")

print("Here is our updated list:")
current = words.head
while current:
    print(current.data)
    current = current.next
print(" ")

print("Let's delete another item.")
print("Was deletion successful?")
words.delete("squash")
print(" ")

print("Here is our list count:")
print(words.count)
print(" ")

print("Here is our updated list:")
current = words.head
while current:
    print(current.data)
    current = current.next
print(" ")


# My version of Agarwal's Circular List 

class Node:
    """ A Circular linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        else:
            print("WE STARTED HERE")
            self.head = node
            self.tail = node
            self.tail.next = self.tail
        self.size += 1

    def delete(self, data):
        current = self.head
        prev = self.head
        flag = True
        while flag or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    #item to be deleted is head node
                    if self.size == 1:
                        self.head = None
                        self.tail = None
                        return
                    self.head = current.next
                    self.tail.next = self.head
                elif current == self.tail:
                    #item to be deleted is tail node
                    self.tail = prev
                    prev.next = self.head
                else:
                    #item to be deleted is an intermediate node
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
            if current == self.head:
                flag = False
        if flag is False:
            print("Item not present in the list")


    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


print("Let's begin the output of the CircularList:")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print(" ")
words = CircularList()
words.append('eggs')
words.append('ham')
words.append('spam')

print("Here are the members of the list, so far, followed by the count.")
counter = 1
for word in words.iter():
    print(word)
    counter += 1
    if counter > words.size:
        break
print(words.size)


print("Let's put some more items in the list.")
print(" ")
words.append('foo')
words.append('bar')
words.append('bim')
words.append('baz')
words.append('quux')
words.append('duux')

print("Which items, and how many, are in the list, now?")
counter = 1
for item in words.iter():
    print(item)
    counter += 1
    if counter > words.size:
        break
print(words.size)
print("")


print("Now we try to delete something that isn't there.")
words.delete('socks')
print("")

print('We check to make sure our list has not changed')
counter = 1
for item in words.iter():
    print(item)
    counter += 1
    if counter > words.size:
        break
print(words.size)
print("")

print('Let us delete something that is there.')
words.delete('ham')
print("")

print('We check to make sure our list has changed accordingly')
counter = 1
for item in words.iter():
    print(item)
    counter += 1
    if counter > words.size:
        break
print(words.size)
print('')


# My version Floyd's Cycle Finding Algorithm

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.tail.next = self.tail
        else:
            self.tail.next = node
            self.tail = node
            node.next = self.head # Toggle this on/off for loop/not
        self.size += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def floydsCycle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while (slow_pointer != None 
                and fast_pointer != None
                and fast_pointer.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if (slow_pointer == fast_pointer):
                print("OK WE BREAK at {}".format(slow_pointer.data))
                return slow_pointer.data

        if (slow_pointer != fast_pointer):
            return None

print('Let us begin the output of Floyd\'s Cycle Finding Algorithm.')
print('----------------------')
print('----------------------')
print('----------------------')
print('----------------------')
words = CircularList()
words.append('eggs')
words.append('ham')
words.append('spam')

print('Let us display the members of the list.')
current = words.head
count = 1
while count <= words.size:
    print(current.data)
    current = current.next
    count += 1

print('')

loop_start = words.floydsCycle()
if (loop_start == None):
    print('List contains no loop.')
else:
    print('List contains a loop at {}'.format(loop_start))


# Attempting Agarwal's SinglyLinkedList again, on 12_27_23

class Node1223:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList1223:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append1223(self, data, location):
        node = Node1223(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        elif location == 0:
            current = self.head
            self.head = node
            node.next = current
            self.size +=1
        else:
            current = self.head
            previous = None
            count = 0
            while count < location-1:
                count += 1
                previous = current
                current = current.next
            if current.next:
                previous = current
                current = current.next
                previous.next = node
                node.next = current
                self.size += 1
            else:
                current.next = node
                self.tail = node
                self.size += 1
    def delete1223(self, location):
        current = self.head
        previous = None
        count = 0
        while count < location:
            previous = current
            current = current.next
            count += 1
        if count == 0:
            self.head = current.next
            self.size -= 1
        else:
            if count+1 == self.size:
                self.tail = previous
                previous.next = None
                self.size -= 1
            else:    
                previous.next = current.next
                self.size -= 1
    def search1223(self, data):
        current = self.head
        count = 0
        while current:
            if current.data == data:
                return "Found {} at position {}".format(current.data, count)
            else:
                current = current.next
                count += 1
        return "That item does not exist in our SinglyLinkedList1223."
    def clear1223(self):
        self.head = None
        self.tail = None
    def traverse1223(self):
        current = self.head
        if current is None:
            return
        while current:
            print(current.data)
            current = current.next

single = SinglyLinkedList1223()

print("")
print("***********SinglyLinkedList on 12_27_23**************")
print("***********SinglyLinkedList on 12_27_23**************")
print("")

print("We begin appending items to the SinglyLinkedList")

print("")
print("List size: {}".format(single.size))
single.append1223("head", 0)
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("List size: {}".format(single.size))
single.append1223("tail", 1)
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("List size: {}".format(single.size))
single.append1223("torso", 1)
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("List size: {}".format(single.size))
single.append1223("neck", 1)
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("List size: {}".format(single.size))
single.append1223("shoulders", 2)
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("List size: {}".format(single.size))
single.append1223("tail_hair", 5)
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("List size: {}".format(single.size))
single.append1223("head_hair", 0)
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("List size: {}".format(single.size))

print("")
print("Now we remove items")

print("")
print("Here is the list size, the list, and the head and tail.")
print("List size: {}".format(single.size))
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("Deleting location 0")
single.delete1223(0)

print("")
print("List size: {}".format(single.size))
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("Deleting location 4")
single.delete1223(4)

print("")
print("List size: {}".format(single.size))
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("Deleting location 4")
single.delete1223(4)

print("")
print("List size: {}".format(single.size))
print("**********LIST:")
single.traverse1223()
print("head and tail: {} -- {}".format(single.head.data, single.tail.data))

print("")
print("Now we search for items in the SinglyLinkedList1223.")

print("")
print("We first search for an item in the list, say torso.")
print(single.search1223("torso"))

print("")
print("Then we search for item not in the list, say 'LIST'.")
print(single.search1223("LIST"))

print("")
print("Let's clear the list.")
single.clear1223()
single.traverse1223()
print("head and tail: {} -- {}".format(single.head, single.tail))


# Attempting Agarwal's DoublyLinkedList again, on 12_30_23

class NodeDoubly1223:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList1223:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append_arbitrary_doubly1223(self, data, location):
        node = NodeDoubly1223(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            current = self.head
            count = 0
            while count < location:
                current = current.next
                count += 1
            if current:
                if current.prev:
                    current.prev.next = node
                    node.prev = current.prev
                    current.prev = node
                    node.next = current
                    self.size += 1
                    return
                else:
                    self.head = node
                    node.next = current
                    current.prev = node
                    self.size += 1
                    return
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1
    def append_at_end_doubly1223(self, data):
        node = NodeDoubly1223(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1
    def delete_doubly1223(self, location):
        current = self.head
        count = 0
        if current is None:
            print("List is empty")
        elif location > self.size or location < 0:
            print("List does not contain an element at this index.")
        elif location == self.size:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        else:
            while count < location:
                current = current.next
                count += 1
            if count == 0:
                self.head = current.next
                self.head.prev = None
                self.size -= 1
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
    def clear_doubly1223(self):
        self.head = None
        self.tail = None
        self.size = 0
    def traverse_doubly1223(self):
        current = self.head
        while current:
            if current.prev:
                print("***current.prev: {}".format(current.prev.data))
            print("***current: {}".format(current.data))
            if current.next:
                print("***current.next: {}".format(current.next.data))
            print("_______________")
            current = current.next
double = DoublyLinkedList1223()

print("")
print("***********DoublyLinkedList on 12_30_23**************")
print("***********DoublyLinkedList on 12_30_23**************")
print("")

print("")
print("Let's add some elements to the list.")

print("")
double.append_at_end_doubly1223("glutes")
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_arbitrary_doubly1223("head", 0)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_arbitrary_doubly1223("hips", 1)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_arbitrary_doubly1223("neck", 1)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_arbitrary_doubly1223("head_hair", 0)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_at_end_doubly1223("tail")
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_arbitrary_doubly1223("tail_hair", double.size)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_arbitrary_doubly1223("torso", 3)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_arbitrary_doubly1223("scalp", 1)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
double.append_at_end_doubly1223("past")
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
print("-_-_-_-_-_-_-_-_-_-")
print("Let's delete an element from the list.")
print("-_-_-_-_-_-_-_-_-_-")

print("")
print("Deleting location: {}".format(double.size))
double.delete_doubly1223(double.size)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
print("-_-_-_-_-_-_-_-_-_-")
print("Let's delete an element from the list.")
print("-_-_-_-_-_-_-_-_-_-")

print("")
print("Deleting location: 5")
double.delete_doubly1223(5)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
print("-_-_-_-_-_-_-_-_-_-")
print("Let's delete an element from the list.")
print("-_-_-_-_-_-_-_-_-_-")

print("")
print("Deleting location: 0")
double.delete_doubly1223(0)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
print("-_-_-_-_-_-_-_-_-_-")
print("Let's delete an element from the list.")
print("-_-_-_-_-_-_-_-_-_-")

print("")
print("Deleting location: -1")
double.delete_doubly1223(-1)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
print("-_-_-_-_-_-_-_-_-_-")
print("Let's delete an element from the list.")
print("-_-_-_-_-_-_-_-_-_-")

print("")
print("Deleting location: 11")
double.delete_doubly1223(11)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head.data, double.tail.data))

print("")
print("-_-_-_-_-_-_-_-_-_-")
print("Let's clear the list.")
print("-_-_-_-_-_-_-_-_-_-")

print("")
double.clear_doubly1223()
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head, double.tail))

print("")
print("Finally, we attempt to delete an item from the empty list.")
double.delete_doubly1223(3)
print("The size: {}".format(double.size))
double.traverse_doubly1223()
print("Head: {} -- Tail: {}".format(double.head, double.tail))


# Attempting Agarwal's CircularLinkedList again, on 01_04_24

class NodeCircular010424: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class CircularLinkedList010424:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append_at_the_end_circle010424(self, data):
        node = NodeCircular010424(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = self.head
            self.head.prev = node
            self.size += 1
    def delete_circle010424(self, location):
        if location == 0:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size -= 1
        elif location == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            self.size -= 1
        else:
            current = self.head
            count = 0
            while count < location:
                current = current.next
                count += 1
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
    def traverse_circle010424(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        print("*******HEAD***********")
        print("self.head: {}".format(self.head.data))
        print("**********************")
        count = 1
        while count <= self.size:
            print("")
            print("current.prev: {}".format(current.prev.data))
            print("current: {}".format(current.data))
            print("current.next: {}".format(current.next.data))
            current = current.next
            count += 1
        print("")
        print("*******TAIL***********")
        print("self.tail: {}".format(self.tail.data))
        print("**********************")
circle = CircularLinkedList010424()

print("")
print("____________________________")
print("Here is the list and its size:")
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("____________________________")
print("Here is the list and its size:")
circle.append_at_the_end_circle010424("the_head_hair")
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("____________________________")
print("Here is the list and its size:")
circle.append_at_the_end_circle010424("the_head")
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("____________________________")
print("Here is the list and its size:")
circle.append_at_the_end_circle010424("the_neck")
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("____________________________")
print("Here is the list and its size:")
circle.append_at_the_end_circle010424("the_torso")
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("____________________________")
print("Here is the list and its size:")
circle.append_at_the_end_circle010424("the_tail")
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("____________________________")
print("Here is the list and its size:")
circle.append_at_the_end_circle010424("the_tail_hair")
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("/////////Let's delete the head///////")
circle.delete_circle010424(0)
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("/////////Let's delete the tail///////")
circle.delete_circle010424(4)
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")

print("")
print("/////////Let's delete an element other than the head and tail///////")
circle.delete_circle010424(2)
circle.traverse_circle010424()
print("The size of the list: {}".format(circle.size))
print("||||||||||||||||||||||||||||")
