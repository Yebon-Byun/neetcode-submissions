# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        if not root:
            return res
        
        while q: # 트리의 레벨을 하나씩 내려가는 반복(Level Traversal)
            rsv = None
            for _ in range(len(q)): # 현재 레벨의 모든 노드를 하나씩 방문
                node = q.popleft()
                if node:
                    rsv = node
                    q.append(node.left)
                    q.append(node.right)

            if rsv:
                res.append(rsv.val)
        return res