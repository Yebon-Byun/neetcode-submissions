class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            comp = target - val
            if comp in seen:
                return [seen[comp], idx]
            seen[val] = idx
        return []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [i, j]