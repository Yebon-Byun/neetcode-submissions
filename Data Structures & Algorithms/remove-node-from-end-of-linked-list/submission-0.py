# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 연결 리스트 뒤집기
        backward, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = backward
            backward = curr
            curr = tmp

        # 2. 뒤에서 n번째 노드를 건너뛰며 다시 뒤집기
        cnt = 1  # 뒤에서 n번째 == 정방향에서는 (length - n + 1)번째
        res, curr = None, backward
        while curr:
            tmp = curr.next

            if cnt == n:
                # 이 노드는 건너뛰고 연결하지 않음
                curr = tmp
                cnt += 1
                continue
            
            curr.next = res
            res = curr
            curr = tmp
            cnt += 1

        return res
