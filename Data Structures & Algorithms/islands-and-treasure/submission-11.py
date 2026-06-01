class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def add_grid(row, col):
            if (row < 0 or
                col < 0 or
                row == ROWS or
                col == COLS or
                grid[row][col] == -1 or
                (row, col) in visit):
                return
            
            q.append([row, col])
            visit.add((row, col))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                add_grid(row + 1, col)
                add_grid(row - 1, col)
                add_grid(row, col + 1)
                add_grid(row, col - 1)
            dist += 1 
            
                    