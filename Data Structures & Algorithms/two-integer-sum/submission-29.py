class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Brute Force(완전탐색)
    # Hash Map(Two Pass)
    # Hash Map(One Pass)
        indicies = {}

        for i, num in enumerate(nums):
            indicies[num] = i
        
        for i, num in enumerate(nums): 
            diff = target - nums[i]
            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]