class Node:
    def __init__(self,value, random=None, next=None):
        self.value = value
        self.random = random
        self.next = next

class LinkedList:
    def __init__(self, value):
        newnode = Node(value)
        self.head, self.tail = newnode, newnode
    
    def copyRandomList(self):
        oldToCopy = {None: None}
        curr = self.head 

        while curr is not None:  # cloning linked list nodes and adding them to the hashmap
            copy = Node(curr.value)
            oldToCopy[curr] = copy 
            curr = curr.next

        curr = self.head 

        while curr is not None:  # pointer connection 
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next  

        return oldToCopy[self.head]
    
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

ll = LinkedList(7)
ll.append(13)
ll.append(11)
ll.append(10)
ll.append(1)
new_head = ll.copyRandomList()
ll.head = new_head
ll.print_list()
