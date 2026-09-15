"""
01.
Let me take a moment to read through the problem
So, I just to make sure that I understand the prob correctly
We're given a prefix tree, and we would like to build a spell checker system with some methods. Correct?

02.
valid input?    Special characters?
empty input?    ""

03.
That should give us O(n) time complexity for each function call and O(t) space complexity.

04.
Let me explain my approach before I coding



"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        
        