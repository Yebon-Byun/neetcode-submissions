# Grid에서 1인 곳을 발견하면 dfs()를 이용해서 좌,우 / 위, 아래 연결된 곳들을 찾아서 island 개수 세기
# dfs()

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r  >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": 
                    dfs(r, c)
                    islands += 1

        return islands
                
        
