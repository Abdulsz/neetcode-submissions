class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ''' 
        -pacific
        -atlantic
        loop and start from the sides
        add them to the respective sets
        use that same set as the duplicate checker

        '''

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        

        def dfs(r,c,ocean,prev):

            if r not in range(ROWS) or c not in range(COLS) or heights[r][c] <prev or (r,c) in ocean:
                return

            ocean.add((r,c))
            cur = heights[r][c]

            dfs(r+1,c,ocean,cur)
            dfs(r-1,c,ocean,cur)
            dfs(r,c+1,ocean,cur)
            dfs(r,c-1,ocean,cur)

        for r in range(ROWS):
            dfs(r,0,pacific,-1)
            dfs(r,COLS-1,atlantic,-1)

        for c in range(COLS):
            dfs(0,c,pacific,-1)
            dfs(ROWS-1,c,atlantic,-1)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res



