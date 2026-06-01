class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            res = 1
            

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        res += 1
            return res
            
        for r in range(ROWS): 
            for c in range(COLS):
                if (grid[r][c] == 1 and (r, c) not in visited):
                    area = max(area, bfs(r, c))
        
        return area




