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
    
    def popFirst(self):
       if self.length  == 0:
           return None
       temp = self.head
       self.head = self.head.next
       temp.next = None
       self.length -= 1
       if self.length == 0:
           return None
       return temp.value 

    def pop(self):
        if self.length == 0:
            return None
        temp,prev = self.head,self.head
        while temp.next is not None:  
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        return temp.value
    
    def prepend(self,data):
        newnode = Node(data)
        if self.length == 0:
            self.head = newnode
        newnode.next = self.head
        self.head = newnode

    def append(self,data):
        newnode = Node(data)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        self.tail.next = newnode 
        self.tail = newnode

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
ll = LinkedList(2)
ele = ll.pop()
print(ele)
ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
ll.prepend(4)
ll.prepend(5)
ll.printList()