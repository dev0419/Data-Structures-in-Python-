#Reverse a sublist
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
    
class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head,self.tail = newnode,newnode
    
    def reverse(self,left,right):
        dummy = Node(0)
        dummy.next = self.head
        leftPrev,curr = dummy,self.head 

        for i in range(left-1):
            leftPrev,curr = curr, curr.next
        
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next
    
    def append(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head,self.tail = newnode,newnode
        self.tail.next = newnode 
        self.tail = newnode 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

new = ll.reverse(2,4)
ll.head = new 
ll.print_list()
