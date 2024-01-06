class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.length = 1
        self.tail,self.head = newnode,newnode

    def printList(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        newnode  = Node(value)
        if self.head is None:
            self.head,self.tail = newnode,newnode
        temp = self.head 
        while temp.next is not None:
            temp = temp.next 
        temp.next = newnode 
        self.length += 1

    def reverseKNodes(self, k):
        dummy = Node(0)
        dummy.next = self.head
        temp = dummy

        while temp.next:
            k_th = self.getK(temp, k)
            if not k_th:
                break
            group_next = k_th.next
            temp_next = temp.next

            prev, curr = k_th.next, temp.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            temp.next = prev
            temp_next.next = group_next
            temp = temp_next

        return dummy.next

    
    def getK(self,curr,k):
        while curr and k > 0:
            curr = curr.next 
            k -= 1
        return curr
    
l = LinkedList(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
k = 2
l.head = l.reverseKNodes(k)
l.printList()
