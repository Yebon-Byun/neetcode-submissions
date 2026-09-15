"""
[01].
Let me take a moment to read through the prob
nums:   unsorted, int arry
return: smalles pos int (not in nums)
in 
O(n) time
O(1) auxiliary space

[02].
valid?
empty?
duplicates?
modification?
constraints?

[03].
Input: nums = [-2,-1,0]
Output: 1

[04].


"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1
                


        