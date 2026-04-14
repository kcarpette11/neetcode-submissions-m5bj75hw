# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using fast and slow pointers to help detect cycles in list

        #initialize pointers

        slow = head
        fast = head 
       

        #move slow once, but move fast twice

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


            if slow == fast:  # if a cycle is detected
                return True 
            
        return False # for output 
        