class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prv = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)          # left, right dummy 노드 만들기!
        self.left.nxt, self.right.prv = self.right, self.left   # 서로 연결하기!

    def insert(self, node):
        prv = self.right.prv
        nxt = self.right
        prv.nxt = nxt.prv = node
        node.prv, node.nxt = prv, nxt

    def remove(self, node):
        prv, nxt = node.prv, node.nxt
        prv.nxt, nxt.prv = nxt, prv


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]



        
