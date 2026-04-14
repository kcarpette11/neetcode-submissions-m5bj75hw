# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #using fast and slow pointer apporoach 

        slow = head # initialize pointers
        fast = head
       

        for i in range(n): # move fast pointer n steps first by iterating
            fast = fast.next

        if fast is None: 
            return head.next 

        #move slow twice, move fast once
        while  fast.next:
            fast = fast.next
            slow = slow.next


            
        
        slow.next = slow.next.next # remove nth node



        
        return head #return beginning of list 

     