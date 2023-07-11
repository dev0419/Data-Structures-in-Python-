class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1 
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode 
        else:
            self.tail.next = newnode
            self.tail = newnode 
            self.length += 1
        return True 
    
    def prepend(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        newnode.next = self.head 
        self.head = newnode
        self.length += 1 
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp 
            temp  = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1 
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def popFirst(self):
        if self.length == 0:
            return None 
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _  in range(index):
            temp = temp.next
        return temp.value
    
    def set_value(self, index, value):
        temp = self.get(index)
        if not isinstance(temp, Node):
            return False
        temp.value = value
        return True
    
        

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.prepend(4)
print('linkedlist:')
ll.printList()
print(f"popped element:{ll.pop()}")
print('linkedlist:')
ll.printList()
print(f"popped element:{ll.popFirst()}")
print('linkedlist:')
ll.printList()
print(f"element at index 0: {ll.get(0)}")
ll.set_value(0,10)
print('linkedlist:')
ll.printList()