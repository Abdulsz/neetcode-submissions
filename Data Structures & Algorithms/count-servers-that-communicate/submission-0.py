class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = [0]*len(grid)
        cols = [0]*len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows[r]+=1
                    cols[c]+=1

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (rows[r]>1 or cols[c]>1):
                    res+=1

        return res
        