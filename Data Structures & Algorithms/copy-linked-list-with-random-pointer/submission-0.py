"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #using hash map 

        if not head: # if head doesn't exist 
            return None

        #initialize hash map 

        hash_map = {} 

        # add pairs to hash map

        current = head 

        while current:
            copy = Node(current.val) # make copied nodes of list
            hash_map[current] = copy
            current = current.next

        current = head
        #assign pointers 
        while current:
            if current in hash_map:
                hash_map[current].next = hash_map.get(current.next)


                pass 
            if current.random:
                hash_map[current].random = hash_map.get(current.random)
            current = current.next
        return hash_map[head]

        


        