# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        #find the middle point
        fast=head
        mid=head
        while fast.next and fast.next.next:
            mid=mid.next
            fast=fast.next.next
        second = mid.next
        mid.next = None
        #reverse mid
        prev=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        second=prev
        #assemble
        first=head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        


        
        