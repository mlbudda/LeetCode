#%%
# 141. Linked List Cycle
# Concept Hashing
# * Success
# Runtime: 56 ms, faster than 41.58%
# Memory Usage: 18.2 MB, less than 5.45%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """ Determines if the linked list has 
        a cycle in it. """
        # Declare map to store node address
        node_map = set()

        # If head is none no cycle is present
        while head is not None:

            # Checking if address is already in map
            if head in node_map:
                return True
            
            # If address not present, insert
            node_map.add(head)
            head = head.next
        return False

