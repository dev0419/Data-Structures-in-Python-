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
        self.tail = newnode
        self.length += 1
    
    def prepend(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head,self.tail = newnode,newnode
        newnode.next = self.head 
        self.head = newnode 
        self.length += 1
    
    def insert(self,index,value):
        if index < 0 or index == self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.head 
        newnode = Node(value)
        for i in range(index - 1):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
        self.length += 1
        return temp 
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.head 
        prev = self.head
        while temp.next is not None:
            prev = temp 
            temp = temp.next
        temp.next = None
        prev.next = temp 
        self.length -= 1
        if self.length == 0:
            self.head,self.tail  = None,None
        return temp
    
    def deleteFirst(self):
        if self.head is None:
            return None
        temp = self.head 
        self.head = self.head.next 
        temp.next = None
        self.length -= 1 
        if self.length == 0:
            self.head,self.tail  = None,None
        return temp
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.deleteFirst()
        if index == self.length - 1:
            return self.pop()
        temp,prev = self.head,None
        for i in range(index):
            prev = temp 
            temp = temp.next
        prev.next = temp.next 
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head,self.tail = None,None 
        return temp 

    def printList(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def reverse(self):
        if self.head is None:
            return None 
        prev,temp = None,self.head
        while temp is not None:
            cur = temp.next
            temp.next = prev
            prev = temp 
            temp = cur
        return prev
            
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.prepend(5)
first_val = ll.insert(0,9)
last_val = ll.insert(5,6)
val = ll.insert(2,8)
ll.printList()
rem_l = ll.pop()
print(f"Deleted value: {rem_l.value}") 
rem_f = ll.deleteFirst()
print(f"Deleted value: {rem_f.value}")
ll.printList()
rem_m = ll.remove(2)
print(f"Deleted value: {rem_m.value}")
ll.printList()
new_head = ll.reverse()
ll.head = new_head 
print("Reversed List:")
ll.printList()