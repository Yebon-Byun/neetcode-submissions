"""
Doubly Linked List


해시맵 + DDL(Doubly Linked List)


[Intuition]:
We want all operations to be O(1) while still following LRU(Least Recently Used, 가장 오랫동안 사용되지 않은) rules.

To do that, we combile:
1. Hash Map -> quickly find a node by its key in O(1)
2. Doubly Linked List -> quickly move nodes to the most recently used position and remove the least recently used node from the other end in O(1)

We keep:
• The most recently used node near the right side.
• The least recently used node near the left side.

Whenever we:
• Get a key: move that node to the right(most recently used)
• Put a key:
    - If it exists: update value and move it to the right
    - if it's new:
        * If at capacity: remove the leftmost real node(LRU)
        * Insert the new node at the right

Dummy left and right nodes make insert/remove logic cleaner


[Algorithm]:
1. Data Structrues
• A hash map cache taht amps key -> node.
• A doubly linked list with:
    - left dummy: before the least recently used node.
    - right dummy: after the most recently used node.

2. Helper: remove(node)
• Unlink node from the list by connecting its prev and next nodes.

3. Helper: insert(node)
• Insert node just before right (mark as most recenlty used)

4. get(key)
• If key not in cache, return -1
• Otherwise:
    - Remove its node from the list
    - Insert it again near right (mark as recently used).
    - Return the node's value.


"""
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return  self.cache[key].val
        return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

"""
■ self.prev = self.next = None

a = b = None          # 안전 (불변 + 이후 재할당만 함)
a = b = 0             # 안전 (숫자도 불변)
a = b = []            # 위험! (변경 가능한 것 공유)
a = b = TreeNode(1)   # 위험! (a.val 바꾸면 b.val도 바뀜 — 같은 객체니까)

"공유한 대상의 속을 바꿀 일이 있는가"가 질문이에요. 속을 바꿀 수 없는 것(None, 숫자, 문자열, 튜플)은 묶어 써도 되고, 속이 있는 것(리스트, dict, 객체)은 묶으면 사고 나요


■ Dummy 노드란?
데이터로서의 의미는 없고 자리만 차지하는 가짜 노드 e.g. Node(0, 0)


"""

        
