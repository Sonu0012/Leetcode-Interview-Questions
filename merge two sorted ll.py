from lib2to3.pytree import Node


def merge(head1,head2):
    temp1,temp2 = head1,head2
    current = mylist = Node(0)
    while temp1 and temp2:
        if temp1.val<temp2.val:
            mylist.next = Node(temp1.val)
            temp1 = temp1.next

        else:
            mylist.next = Node(temp2.val)
            temp2= temp2.next

        mylist= mylist.next    

    while temp1:
        mylist.next=Node(temp1.val)
        temp1 = temp1.next
        mylist = mylist.next           
    
    while temp2:
        mylist.next=Node(temp2.val)
        temp2 = temp2.next
        mylist = mylist.next 

    return current.next    
