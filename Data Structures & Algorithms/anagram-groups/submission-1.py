class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Sorting
        dict_strs = defaultdict(list)
        for word in strs:
            word_sorted = sorted(word)
            join_word = "".join(word_sorted)
            dict_strs[join_word].append(word)
        return list(dict_strs.values())