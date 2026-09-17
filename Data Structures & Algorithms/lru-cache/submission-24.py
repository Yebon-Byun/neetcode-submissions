class Node:
    # Store a key-value pair and pointers
    # for the doubly linked list.
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        # Step 1: Use a hash map for O(1) key lookup,
        # and a doubly linked list to track recency.
        self.capacity = capacity
        self.cache = {}

        # Dummy head = least recently used side
        # Dummy tail = most recently used side
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    # Step 2: Insert a node right before the tail,
    # making it the most recently used node.
    def insert(self, node):
        prev_node = self.tail.prev
        next_node = self.tail

        prev_node.next = node
        next_node.prev = node

        node.prev = prev_node
        node.next = next_node

    # Step 3: Remove a node from the doubly linked list.
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        # Step 4: If the key exists, move it to the
        # most recently used position and return its value.
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        # Step 5: If the key already exists,
        # remove its old node from the list.
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new node and mark it as most recently used.
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Step 6: If we exceed capacity,
        # evict the least recently used node.
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]