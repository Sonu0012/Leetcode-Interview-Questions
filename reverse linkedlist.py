def reverse(head):
    prev = None
    current = head

    while current:
        nextnode = current.next
        current.next = prev
        prev= current
        current = nextnode

    return prev    