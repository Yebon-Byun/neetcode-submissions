class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Start with two pointers at the end of sorted array
        left, right = 0, len(numbers)-1

        # Evaluate the current pair without trying every combination
        while left < right:
            total = numbers[left] + numbers[right]
        
            if total < target:
                left += 1
            
            elif total > target:
                right -= 1
            
            else:
                return [left+1, right+1]
        
        return []