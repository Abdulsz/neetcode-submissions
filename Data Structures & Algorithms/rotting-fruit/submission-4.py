class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        minutes = 0
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1

                if grid[r][c] == 2:
                    q.append((r,c))
        if fresh == 0:
            return 0

        while q:
            minutes+=1
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr = dr+r
                    nc = dc+c

                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        fresh-=1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                    
            if fresh == 0:
                return minutes

        return -1
            




