# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if k == 1 or not head:
        return head
    
    stack = []
    dummy = ListNode(0)
    prev = dummy
    curr = head
    
    while curr:
        count = 0
        temp = curr
        
        # Push k nodes to stack
        while temp and count < k:
            stack.append(temp)
            temp = temp.next
            count += 1
        
        # If we don't have k nodes, break
        if count < k:
            prev.next = curr
            break
        
        # Pop from stack to reverse
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        
        curr = temp
        prev.next = None
    
    return dummy.next

       

        