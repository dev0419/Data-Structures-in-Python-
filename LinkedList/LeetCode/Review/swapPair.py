class Node:
    def __init__(self,value):
        self.value = value
        self.next = None   

class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head,self.tail = newnode,newnode
        self.length = 1
    
    def swapPair(self):
        dummy = Node(0)
        dummy.next = self.head 
        prev,curr = dummy,self.head
        while curr and curr.next is not None: #We want to atleast reverse 2 nodes not just one node 
            #save ptrs 
            nxtPair = curr.next.next #next pair of nodes to get swapped
            second = curr.next #second node

            #reverse
            second.next = curr 
            curr.next = nxtPair
            prev.next = second #first and second ptrs are swapped 

            #update ptrs
            prev = curr 
            curr = nxtPair

        return dummy.next
    
    def append(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head,self.tail = newnode,newnode 
        self.tail.next = newnode 
        self.tail = newnode
        self.length += 1
        return True 
    
    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
new_head = ll.swapPair()
ll.head = new_head
ll.print_list()
