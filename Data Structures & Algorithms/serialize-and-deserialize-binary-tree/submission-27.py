"""
BFS

■ deque([root]):
deque(...)의 괄호 안에 들어가는 건 "deque에 넣을 원소들"이 아니라 "원소를 꺼내올 iterable"이에요.
deque(root)     # TypeError: 'TreeNode' object is not iterable
deque([root])   # OK: "root 하나가 든 리스트"를 순회해서 root를 담음

[Intuiton]:
Instead of using DFS, we treat the tree like a queue(level order traversal)
BFS visits nodes level by level, so we simply record values in that order:
• if a node exists - record its value and push its children(even if they are None).
• if a node is missing - record "N" to mark empty spots.

This ensures the structure is preserved, because BFS processes nodes exactly how they appear in the tree layout

During deserialization, we again use BFS:
• The first value is the root.
• Then for each node in the queue, assign its left and right children from the next values in the list.

This keeps the tree reconstruction aligned with the serialized order.


[Algorithm]:

Serialize
1. If root is None - return "N"
2. Initialize a queue with root
3. While queue is not empty:
• pop a node
• if node exists - append its value, push left & right children
• if node is missing - append "N"
4. Join the list with commas and return

Deserialize
1. Split string into list vals
2. If first value is "N" - return None
3. Create root from list value and push it into a queue
4. Use an index to read the next values:
• For each node popped from queue:
- If vals[index] is not "N" - create left child & push
- Move index
- Repeat for right child
5. Return the root of the rebuilt tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index +=1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root

