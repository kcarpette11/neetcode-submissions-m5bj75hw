# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) <= 0 or not lists:
            return None
        res = lists[0]

        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res, lists[i])
        return res
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # create dummy node to keep track of the head

            dummy = ListNode(0)
            curr = dummy # current node is the dummy

            while list1 and list2: # move through the list
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            # attach any nodes onto any of the two lists
            curr.next = list1 or list2
            return dummy.next # returns head of linked list


            