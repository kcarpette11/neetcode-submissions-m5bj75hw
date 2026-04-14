# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #using the fast and slow pointer approach to divide the list


        #initialize pointers

        slow, fast = head, head
       
         #move slow once, move fast twice 
        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next 
        #reversing second half of array 

        prev, curr = None, slow # more pointers

        while curr: # borrowing from reverse linked list
            new_node = curr.next
            curr.next = prev 
            prev = curr
            curr = new_node

        #merging 2 halves
        first, second = head, prev
        while second and second.next:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second








        

      
        


        