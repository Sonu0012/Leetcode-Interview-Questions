def removeduplicate(head):
    temp = head
    if head == None:
        return head

    while temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next

        else:
            if temp.next:
                temp = temp.next

    return head            
