class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            comp = target - val
            if comp in seen:
                return [seen[comp], idx]
            seen[val] = idx
        return []

                