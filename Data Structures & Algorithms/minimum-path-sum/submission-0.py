"""
Dynamic Programming(Bottom-Up)


[Intuition]:
Instead of recursing from top-left to bottom-right, we can fill a DP table starting from the bottom-right corner. For each cell, we know the minimum path sum to reach the destination from the cell below and from the cell to the right. We take the minimum of these two and add the current cell value. Thks iterative approach avoids recusion overhead.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS] = 0
        print("dp", dp)

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = grid[r][c]  + min(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]
        