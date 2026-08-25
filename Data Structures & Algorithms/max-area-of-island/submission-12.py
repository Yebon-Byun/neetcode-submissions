class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            
            return res


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:      
                    max_area = max(max_area, bfs(row, col))

        return max_area