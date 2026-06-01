# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] #결과
        q = deque() #대기목록
        q.append(root)
    
        if not root:
            return res

        while q: 
            level = [] #결과에 포맷을 맞추기 위한 도움 리스트
            for curr in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res

                    
                

            