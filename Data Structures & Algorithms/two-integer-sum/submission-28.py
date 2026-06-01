class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Brute Force(완전탐색)
    # Hash Map(Two Pass)
    # Hash Map(One Pass)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]