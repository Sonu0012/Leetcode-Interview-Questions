from lib2to3.pytree import Node


#my solution
def adder(l1,l2):
    mylist = current = Node(0)
    temp1,temp2 = l1,l2
    carry = 0
    while temp1 and temp2:
        if temp1.val + temp2.val + carry >=10:
            mylist.next = Node((temp1.val+temp2.val)%10)
            carry = int((temp1.val + temp2.val + carry)/10)

        else:
            mylist.next = Node((temp1.val + temp2.val + carry)%10)
            carry = 0
        temp1 = temp1.next
        temp2 = temp2.next    
        mylist = mylist.next

    while temp1:
        if temp1.val+carry>=10:
            mylist.next = Node((temp1.val+carry)%10)
            carry = int((temp1.val + carry)/10)
           
        else:
            mylist.next = Node((temp1.val + carry)%10)
            carry = 0
        temp1 = temp1.next    
        mylist = mylist.next

    while temp2:
        if temp2.val+carry>=10:
            mylist.next = Node((temp2.val+carry)%10)
            carry = int((temp2.val + carry)/10)
           
        else:
            mylist.next = Node((temp2.val + carry)%10)
            carry = 0
        temp2 = temp2.next    
        mylist = mylist.next

    if carry>0:
        mylist.next = Node(carry)

    return current.next   



#Some tactics in the solution
def adder1(l1,l2):
    carry = 0
    current = mylist = Node(0)
    while l1 or l2 or carry:
        v1 = v2 = 0 
        if l1:
            v1 = l1.val
            l1 = l1.next

        if l2:
            v2 = l2.val                         
            l2 = l2.next

        carry , val = divmod(v1+v2+carry,10)

        current.next = Node(val)
        current = current.next     

    return mylist
