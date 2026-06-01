class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        
        for i, n in enumerate(nums):
            indicies[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]
        return []



        return indicies
                
                    
