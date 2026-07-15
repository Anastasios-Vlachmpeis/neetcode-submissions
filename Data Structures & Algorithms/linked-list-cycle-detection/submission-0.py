# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []

        while head  :
            if head in arr:
                return True
            arr.append(head)
            head = head.next

        return False