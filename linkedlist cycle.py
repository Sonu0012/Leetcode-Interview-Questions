
def ll1(head):
    temp = head
    a = []

    if head == None:
        return False

    while temp.next not in a and temp.next:
        a.append(temp.next)
        temp = temp.next
        if temp.next in a:
            return True
    return False


def ll2(head):
    try:
        slow = head
        fast = head.next

        while slow is not fast:
            slow = slow.next
            fast = fast.next.next

        return True

    except:
        return False                    