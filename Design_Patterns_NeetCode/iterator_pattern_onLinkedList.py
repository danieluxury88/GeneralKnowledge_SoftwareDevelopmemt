class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None

    #Define Iterator
    def __iter__(self):
        self.cur = self.head
        return self
    

    #Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration
        

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
my_list = LinkedList(head)

for node in my_list:
    print(node)

    

    