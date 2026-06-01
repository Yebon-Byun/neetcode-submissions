# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        
        while q:
            right_view = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right_view = node
                    q.append(node.left)
                    q.append(node.right)
                
            if right_view:
                res.append(right_view.val)
            
        return res
                    
