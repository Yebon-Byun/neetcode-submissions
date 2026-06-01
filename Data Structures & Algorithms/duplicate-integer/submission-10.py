class Solution:
    # Brute Force
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False

    # Hash Set
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     sorted_nums = sorted(nums)
    #     for i in range(1, len(nums)):
    #         if sorted_nums[i] == sorted_nums[i - 1]:
    #             return True
    #     return False

    # Hash Set(length)
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) == len(nums):
            return False
        return True

