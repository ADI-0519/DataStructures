
class ListNode:
    def __init__(self,data = 0):
        self.val = data
        self.next = None

    
    

class LinkedList:
    def __init__(self):
        #Head points to start of linked list
        self.head = ListNode()
        

    def add(self,data):
        new_node = ListNode(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next

        cur.next = new_node


    def length():
        
