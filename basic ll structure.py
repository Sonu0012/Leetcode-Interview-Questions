class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next


l1 = Linkedlist()
l1.head=Node(5)
second = Node(7)
third = Node(9)
l1.head.next = second
second.next = third


l2 = Linkedlist()
l2.head = Node(3)
s = Node(6)
t= Node(8)
f = Node(13)

l2.head.next = s
s.next = t
t.next = f


print(l1.printlist())
print(l2.printlist())



