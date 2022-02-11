from lib2to3.pytree import Node


def remove(head,val):
    dummy = Node(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next

        else:
            current = current.next

    return dummy.next            