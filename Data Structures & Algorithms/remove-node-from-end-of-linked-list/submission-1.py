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
        res, curr = None, backward
        while curr:
            if cnt == n:
                cnt += 1
                curr = curr.next
                continue
            else:
                tmp = curr.next
                curr.next = res
                cnt += 1
            res = curr
            curr = tmp
        
        return res


        # cnt = 0
        # prev, res = None, backward
        # while backward:
        #     print(backward.val)
        #     if cnt == n-1:
        #         backward = backward.next
        #     tmp = backward.next
        #     backward.next = prev 
        #     prev = res
        #     res = tmp
        #     cnt += 1

            



        # while backward:
        #     if cnt == n-1:
        #         tmp = backward.next.next          
        #     else:
        #         tmp = backward.next
        #     backward = backward.next
        #     cnt += 1
        
        # return res 

        
    