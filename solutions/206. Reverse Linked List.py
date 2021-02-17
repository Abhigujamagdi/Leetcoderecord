# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        next = None
        current = head
        previous= None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
        
