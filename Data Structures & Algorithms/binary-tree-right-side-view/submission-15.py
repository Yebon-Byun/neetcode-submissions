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
            rightSide = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res



        ####
        # [1,2,3,4] case haven't been able to pass
        # I think I couldn't access TreeNode(2) because I've never seen 4 in result
        # only result I've got is [1,3]

        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
                    
        #         if node:
        #             if len(q) > 0:
        #                 continue
        #             else: 
        #                 res.append(node.val)
        #             if node.left != None:
        #                 level.append(node.left)
        #             if node.right != None:
        #                 level.append(node.right)
        #             if level:
        #                 q.append(level[-1])
        #     level = []
                    




        #####
        # good try tho, got a case that I could thought of 
        # I tried DFS, but I think I should give it a shot with BFS
        # res = []

        # if not root:
        #     return res
        
        # while root:
        #     res.append(root.val)
        #     if root.right:
        #         root = root.right
        #     else: 
        #         root = root.left
            
        
        # return res
            