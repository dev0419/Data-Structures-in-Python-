class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head,self.tail = newnode,newnode
        self.length = 1
    
    def append(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head,self.tail = newnode,newnode
        temp = self.head
        while temp.next is not None:
            temp = temp.next 
        temp.next = newnode
        self.length += 1
        
    def prepend(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head,self.tail = newnode,newnode
        newnode.next = self.head 
        self.head = newnode 
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        prev,temp = None,self.head
        while temp.next is not None:
            prev = temp 
            temp = temp.next 
        prev.next = None 
        self.length -= 1
        if self.length == 0:
            self.head,self.tail = None,None

    def deleteFirst(self):
        if self.head is None:
            return None
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        self.length -= 1 
        if self.length == 0:
            self.head,self.tail = None,None
    
    def printList(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def insert(self,value,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newnode = Node(value)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        newnode.next = temp.next 
        temp.next = newnode
        self.length += 1
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.deleteFirst()
        if index == self.length - 1:
            return self.pop() 
        temp = self.head 
        prev = None
        for i in range(index):
            prev = temp 
            temp = temp.next
        prev.next = temp.next 
        temp.next =  None  
        self.length -= 1

    def reverse(self):
        if self.head is None:
            return None
        curr,prev = self.head,None
        while curr is not None:        
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp 
        return prev

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.pop()
ll.deleteFirst()
ll.insert(1,1)
ll.remove(1)
new_head = ll.reverse()
ll.head = new_head 
print("Reversed List:")
ll.printList()
