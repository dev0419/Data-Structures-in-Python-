class Node:
    def __init__(self,value):
        self.value = value 
        self.next,self.prev = None,None

class DoublyLinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head,self.tail = newnode,newnode
        self.length = 1

    def reverse(self):
        temp = None 
        curr = self.head 
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp 
            curr = curr.prev
        if temp is not None:
            self.head = temp.prev

    def append(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head,self.tail = newnode,newnode
        self.tail.next = newnode 
        newnode.prev = self.tail
        self.tail = newnode 
        self.length += 1

    def print_list(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next

ll = DoublyLinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.reverse()
ll.print_list()





        