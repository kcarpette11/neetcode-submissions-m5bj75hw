# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        curr = head # for reverse linked lists

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
       # build result in forward order

        dummy = ListNode(0)
        current = dummy
       
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val  // 10
            val = val % 10

            current.next = ListNode(val) # Add to end of the list
            current = current.next
            

        # move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


        