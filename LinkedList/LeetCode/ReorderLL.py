#Reorder linked list  
#Use 2ptr approach 
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode 
        self.tail = newnode 
    
    def append(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head, self.tail = newnode, newnode 
        self.tail.next = newnode
        self.tail = newnode 
    
    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next 
        
    def reorder(self):
        slow,fast = self.head,self.head.next
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next 
        
        #second half of the list 
        second = slow.next
        slow.next = None 
        prev = None #the list is split into 2
        
        #reversing

        while second is not None:
            temp = second.next 
            second.next = prev
            prev = second 
            second = temp 

        #merge both sublists 
        first,second = self.head,prev 

        while second is not None:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first = temp1 
            second = temp2 

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.reorder()
ll.print_list()


