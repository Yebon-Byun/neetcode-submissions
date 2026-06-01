class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = defaultdict(int)
        for num in nums:
            s[num] += 1
        sortedS = sorted(s.items(), key=lambda x:x[1], reverse=True)
        lst_sorted = [v[0] for v in sortedS]
        return lst_sorted[:k]
        
    
   
            