class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = defaultdict(int)
        res = []
        
        for num in nums:
            storage[num] += 1 

        for i in range(k):
            max_num = max(storage, key=storage.get)
            res.append(max_num)
            storage.pop(max_num)
        
        return res