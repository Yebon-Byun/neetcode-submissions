class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0
        
        while l < r:
            if height[l] <= height[r]:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            
            elif height[l] > height[r]:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
            
        return res
        