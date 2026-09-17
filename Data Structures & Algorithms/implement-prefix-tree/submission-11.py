"""
01. UNDERSTANDING
Let me take a moment to read through the problem
So, I just to make sure that I understand the prob correctly
We're given a prefix tree, and we would like to build a spell checker system with some methods. Correct?


02. QLARIFYING QUESTION
valid input?    Special characters?
empty input?    ""


03. EDGE CASES / EXAMPLES


04. APPROACH / INTUITION
Let me explain my approach before I coding.

- Use a Trie(TrieNode)
- Each node stores children dict and its end_of_word flag

I think we can solve this efficiently, using a trie where each node stores its children in a hash map and end_of_word flag. 
The idea is I'll traverse character by character for all three operations. insert creates missing nodes, search also checks the end-of-word flag, and startWith only checks whether the prefix path exists.

05. TIME / SPACE
That should give us O(n) time complexity for each function call and O(t) space complexity.


06. TESTING
Let me quick dry-run this with the sample input.


07. CODING
code out loud


08. FINAL CHECK


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





        
        