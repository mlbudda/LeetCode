#%%
# 141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        checked = set()
        while head is not None:
            if head in checked:
                return True
            checked.add(head)
            head = head.next
        return False

