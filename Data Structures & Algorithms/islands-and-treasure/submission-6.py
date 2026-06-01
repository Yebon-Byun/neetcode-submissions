class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit =set()
        
        def add_grid(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == -1 or
                (r, c) in visit):
                return
                
            q.append([r, c])
            visit.add((r, c))

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
    
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_grid(r + 1, c)
                add_grid(r - 1, c)
                add_grid(r, c + 1)
                add_grid(r, c - 1)
            dist += 1