class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
    
        return res
        

# backtrack(0, [])
#     include 1 -> subset = [1]
#         backtrack(1, [1])
#             include 1 -> subset = [1, 1]
#                 backtrack(2, [1, 1])
#                     include 2 -> subset = [1, 2, 2]
#                         backtrack(3, [1,1,2]) -> 저장
#                     exclude 2
#                         backtrack(3, [1, 1]) -> 저장
#             exclude 중복 1
#                 backtrack(3, [1]) -> 저장

                    
                    
