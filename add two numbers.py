# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head1 = ListNode(2, ListNode(4, ListNode(6)))
head2 = ListNode(5, ListNode(6, ListNode(4, ListNode(7))))

def printfunc(head):
    cur = head
    while(cur):
        print(cur.val)
        cur = cur.next

def addTwoNumbers(l1, l2):
    cur1 = l1
    cur2 = l2
    head= None
    upper = False

    while cur1 and cur2:
        val = cur1.val + cur2.val
        if upper == True:
            val +=1
            upper =False
        if val>=10:
            val-=10
            upper=True
        if head == None:
            head = ListNode(val)
            cur = head
        else:
            cur.next = ListNode(val)
            cur=cur.next
        cur1 = cur1.next
        cur2 = cur2.next
    while cur1:
        val = cur1.val
        if upper == True:
            val +=1
            upper= False
        if val>=10:
            val-=10
            upper = True
        cur.next = ListNode(val)
        cur=cur.next
        cur1=cur1.next
    while cur2:
        val = cur2.val
        if upper == True:
            val +=1
            upper= False
        if val>=10:
            val-=10
            upper = True
        cur.next = ListNode(val)
        cur=cur.next
        cur2=cur2.next
    if upper = True:
        cur.next = ListNode(1)
    return head

# printfunc(head1)
# printfunc(head2)
printfunc(addTwoNumbers(head1, head2))