class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            anagram[tuple(count)].append(word)
        
        return list(anagram.values())
        
