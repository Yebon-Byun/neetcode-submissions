class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, fixed_number in enumerate(nums):
            if fixed_number > 0:
                break
            
            if idx > 0 and fixed_number == nums[idx - 1]:
                continue
            
            left, right = idx + 1, len(nums) - 1
            while left < right:
                three_sum = fixed_number + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                
                elif three_sum < 0:
                    left += 1
                
                else:
                    res.append([fixed_number, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                        
        return res
            
