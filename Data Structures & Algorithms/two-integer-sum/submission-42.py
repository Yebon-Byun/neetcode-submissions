class Solution:
    # Brute Force
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

    # Hash map(one pass)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in seen:
        #         return [seen[diff], i]
        #     seen[n] = i
        #     print(seen)
             
    # Hash map(two pass)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}

        for i, n in enumerate(nums):
            indicies[n] = i

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]

        return []

            


            
