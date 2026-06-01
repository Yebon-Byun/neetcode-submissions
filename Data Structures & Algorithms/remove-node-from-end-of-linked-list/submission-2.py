# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        backward, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = backward
            backward = curr
            curr = tmp
        
        cnt = 1
        forward, curr = None, backward
        while curr:
            if cnt == n:
                curr = curr.next
                cnt += 1
                continue
            else: 
                tmp = curr.next
                curr.next = forward
            forward = curr
            curr = tmp
            cnt += 1 
        
        return forward
        
        
        