# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr :
            curr = curr.next
            length += 1

        countmax = 0
        curr = head

        if length - n == 0:
            return head.next 

        while curr :
            countmax += 1

            if countmax == length - n:
                curr.next = curr.next.next
                break

            curr = curr.next
            
        return head