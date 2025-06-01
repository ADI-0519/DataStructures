
class ListNode:
    def __init__(self,data = 0):
        self.val = data
        self.next = None

    
    

class LinkedList:
    def __init__(self):
        # Head points to start of linked list
        self.head = ListNode()
        self.tail = self.head
        

    def add(self,data):
        new_node = ListNode(data)
        self.tail.next = new_node
        self.tail = new_node


    def length(self):
        cur = self.head.next
        len = 0
        while cur:
            len += 1
            cur = cur.next

        return len
    

    def traverse(self):
        cur = self.head.next
        while cur:
            print(cur.val)
            cur = cur.next



    
l1 = LinkedList()
l1.add((3))
l1.add((5))
l1.add((8))

print(l1.length())
l1.traverse()