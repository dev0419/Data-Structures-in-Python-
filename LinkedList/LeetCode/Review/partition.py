#List partitioning 
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
    
class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head,self.tail = newnode,newnode
        
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
    
    def partition(self,n):
        left,right = Node(0),Node(0)
        ltail,rtail = left,right 
        
        while self.head is not None:
            if self.head.value < n:
                ltail.next = self.head 
                ltail = ltail.next 
            else:
                rtail.next = self.head 
                rtail = rtail.next
            
            self.head = self.head.next

        ltail.next = right.next
        rtail.next = None         
        return left.next

ll = LinkedList(1)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(5)
ll.append(2)

new_head  = ll.partition(3)
ll.head  = new_head
ll.print_list()

    
