class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = {n:0 for i, n in enumerate(nums)}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1

        k_elements = sorted(nums_dict, key=nums_dict.get, reverse=True)[:k]
        return k_elements
