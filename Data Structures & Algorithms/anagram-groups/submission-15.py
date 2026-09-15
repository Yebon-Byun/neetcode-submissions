"""
[01]
Let me take a moment to read the problem
so I just to make sure I understand this correctly.
we're given an array of strings, and we need to return angrams into sublists.

[02]
valid 
empty 
duplicates
modify
constraints

[03]
For this input, I would expect ... correct?

[04]
Let me explain my approach before I start coding
I think we can solve this effieciently using hashset
The idea is to use hashset and character-to-index mapping.
I'll use a fixed-size array of 26 elements to count character frequencies.

[05]
This should give us O(m * n) time complexity and O(m * n)

[06]
code out loud

[07] Testing / Dry-run
Let me quick dry-run this with the sample

[08] Final Check

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            char_to_idx = [0] * 26
            
            for char in word:
                char_to_idx[ord(char) - ord('a')] += 1
            
            res[tuple(char_to_idx)].append(word)
        
        return list(res.values())

            
        

# Time:
# O(m * n)

# Space:
# O(m) auxiliary space, excluding the returned output
# O(m * n) total space if the output groups are counted













