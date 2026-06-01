# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)

        while q: # q = [2, 3]
            level = [] # level = [1]
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res


    
"""
while solving
BFS
DFS
재귀를 사용하면서 늘어나는 node 개수를 어떻게 계속 넣는거지?
'root를 만나면 왼쪽 오른쪽으로 나눠져서 재귀적으로 진행하며 같은 레벨에 담기' 가능한가?

after solution
- BFS 생각은 했는데, input이 리스트로 들어왔는데 나는 이걸 트리로만 생각을 해서
  리스트를 for loop를 돌리면서 root.left, root.right에 접근이 가능할거란 생각을 못했다.
  잘 생각해보면 그게 맞는데..
- 트리에서 BFS는 항상 큐(Queue) 자료구조를 사용해서, 
  현재 노드의 자식들을 차례로 저장해두고 순서대로 꺼내며 탐색해요. 
"""