# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #mine
        res = []
        res.append(root.val)

        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                res.append(node.left.val)
            if node.right:
                q.append(node.right)
                res.append(node.right.val)
        res = sorted(res)[k-1]

        return res

            

