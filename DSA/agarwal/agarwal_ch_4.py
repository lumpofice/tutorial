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
