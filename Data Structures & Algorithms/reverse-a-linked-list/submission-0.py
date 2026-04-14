# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #initialize pointers
        prev = None
        curr = head

        while curr:
            #save the next node
            temp = curr.next
            curr.next = prev # reverse current nodes's pointer 
            prev = curr # move pointers one step forward
            curr = temp
        return prev # prev is the new head 
        