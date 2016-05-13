from copy import deepcopy

class Node(object): 
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def set_data(self, data):
        self.data = data
        
    def set_next(self, next):
        self.next = next
        

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    
    # O(n)    
    def insert_at_last(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        head = self.head
        while head.next:
            head = head.next
        
        head.next = node
        
    
    # O(1)
    def insert_at_front(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    # worst case will be insertion at the last position
    # so O(n)
    def insert_at_position(self, data, pos):
        if pos<=1:
            self.insert_at_front(data)
            return
        
        count = 1
        prev = None
        head = self.head
        while count != pos:
            prev = head
            head = head.next
            count = count + 1
        
        node = Node(data)
        prev.next = node
        node.next = head
        
        
    # O(n)
    def display(self):
        curr = deepcopy(self.head)
        while curr:
            print str(curr.data) + " --> ",
            curr = curr.next
        print    

    # Only one operation
    # O(1)
    def delete_front(self):
        if not self.head:
            raise Exception("List Empty!!")
        
        self.head = self.head.next

    # O(n)
    def delete_last(self):
        if not self.head:
            raise Exception("List Empty!!")
        
        prev = None
        head = self.head
        while head.next:
            prev = head
            head = head.next
        if not prev:
            self.head = None
        else:
            prev.next = None
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_front(1)
    ll.display()
    ll.delete_last()
    ll.insert_at_last(2)
    ll.insert_at_last(5)
    ll.insert_at_front(8)
    ll.display()
    ll.insert_at_last(4)
    ll.insert_at_last(1)
    ll.display()
    ll.insert_at_front(3)
    ll.insert_at_front(9)
    ll.insert_at_position('a', 3)
    ll.insert_at_position('b', 1)
    ll.display()
    ll.delete_front()
    ll.delete_last()
    ll.display()
    
                