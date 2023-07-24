class Node:
    def __init__(self,key=-1,val=-1,next=None):
        self.key = key
        self.next = next
        self.val = val

class HashMap:
    def __init__(self):
        self.map = [Node() for i in range(1000)]

    def hash(self,key):
        return key%len(self.map)
    
    def put(self,key,value): 
        curr = self.map[self.hash(key)]
        while curr.next is not None:
            if curr.next.key == key:
                curr.val = value
                return
            curr = curr.next
        curr.next = Node(key,value) 

    def get(self,key):
        curr = self.map[self.hash(key)]
        while curr is not None:
            if curr.key == key:
                return curr.val
            curr = curr.next 
        return -1 
    
    def remove(self,key):
        curr =  self.map[self.hash(key)]
        while curr and curr.next is not None:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next 

h = HashMap()
h.put(1000, 12)
h.put(1200, 10)
ob = h.get(1000)
print(ob)  # Output: 12

h.remove(1000)  # Corrected line, removing key 1000 from the hash map
print(h.get(1000))  # Output: -1 (Key is no longer present)

                
