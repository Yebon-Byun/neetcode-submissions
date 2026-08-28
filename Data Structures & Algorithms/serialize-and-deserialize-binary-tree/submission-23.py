"""
DFS

■ [Q1. encodes a tree to a single string 하는 건 알겠는데 which string??]:
아무 문자열이나 마음대로

■ [Q2. serialize? null이 N으로 변한 거 말고는 없는 거 같은데]:
serialize = 메모리 속 객체 구조를 문자열(또는 바이트) 하나로 바꾸는 것
e.g. 
객체(TreeNode()) + 포인터(self.left/self.right)(메모리에만 존재) 
→ 
"1,2,N,N,3,4,N,N,5,N,N" (그냥 텍스트)

■ 이런 문제를 design 문제라고 부름.(146 LRU Cache도 같은 유형). 이런 유형이 나오면 코딩 시작 전에 각 메서드의 입력 타입과 출력 타입을 소리내서 정리하는 게 Clarify 단계.


[Intuition]:
We want to turn a tree into a string(serialize) and then rebuild the same tree from that string(deserialize).

We use preorder DFS(root - left - right) because it naturally records a node before its children

• When a node exists - record its value
• When a child is missing - record "N" so we know where null pointers are.

Example:
1,2,N,N,3,N,N uniquely represents a tree.

During deserialization, we read the list in order:

• "N" - return None
• Otherwise - create node, then build left, then right.

This works because preorder always visits nodes in the exact structure order.


[Algorithm]:

Serialize:
1. Use dfs preorder.
2. if node is null - append "N"
3. Else append node value.
4. Recursively process left child, then right child.
5. Join list with commas - return string

Deserialize:
1. Split string into list vals.
2. Use an index to process values in order.
3. If current value is "N" - return None
4. Otherwise create a node.
5. Recursively build left subtree.
6. Recursively build right subtree.
7. Return the root.

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
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1 
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


