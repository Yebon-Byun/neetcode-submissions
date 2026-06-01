class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Brute Force
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
    
    # 2
        # if sum(nums) == target:
        #     return [i for i in range(len(nums)) if nums[0]]

        # for index, num in enumerate(nums):
        #     diff = target - num
        #     if diff in nums:
        #         index_diff = nums.index(diff)
        #         return [index, index_diff]

    # 3
        indicies = {}
        for i, n in enumerate(nums):
            indicies[n] = i
        
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]
        
