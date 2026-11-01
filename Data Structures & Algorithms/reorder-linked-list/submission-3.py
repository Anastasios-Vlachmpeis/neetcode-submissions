# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        m1, m2 = head, head.next

        while m2 and m2.next :
            m1 = m1.next # One jump at a time
            m2 = m2.next.next # 2 jumps at a time

        two = m1.next
        back = m1.next = None
        
        while two :
            temp = two.next
            two.next = back
            
            back = two
            two = temp

        one, two = head, back

        while two :
            temp, tempv2 = one.next, two.next
            one.next = two
            two.next = temp
            one, two = temp, tempv2

        
            