class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
    
    # Sorting
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False
    
    # Hash set
        # seen = set()
        # print("seen: ", seen)
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        #     print("seen: ", seen)
        # return False
        
    # Hash Set Length
        return len(set(nums)) < len(nums)
            


