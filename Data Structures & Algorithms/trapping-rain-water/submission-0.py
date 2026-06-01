from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0

        for i in range(1, n - 1):
            left_max = max(height[:i])     # 왼쪽 최고 높이
            right_max = max(height[i+1:])  # 오른쪽 최고 높이

            min_height = min(left_max, right_max)

            if min_height > height[i]:
                total_water += min_height - height[i]

        return total_water
