class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 0                      # 갈 수 없는 곳의 면적 기여는 0
            grid[row][col] = 0                # sink (대입!)
            area = 1                          # 나 자신 1칸
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)   # 네 방향이 세온 것을 합산
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:       # 땅에서만 발사
                    max_area = max(max_area, dfs(row, col))

        return max_area