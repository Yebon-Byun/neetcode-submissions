class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        def dfs(r, c):
            cells = 0
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            cells = 1
            for dr, dc in directions:
                cells += dfs(dr+r, dc+c)

            return cells
                


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area