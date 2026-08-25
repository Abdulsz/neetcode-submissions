class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        trie = {}
        

        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
        
            cur['#'] = word

        
        res = []
        visited = set()
        def dfs(r,c,t):
            
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or board[r][c] not in t:
                return

            t = t[board[r][c]]
            if '#' in t:
                word = t['#']
                del t['#']
                res.append(word)

            
            visited.add((r,c))
            
            dfs(r+1,c,t)
            dfs(r-1,c,t)
            dfs(r,c+1,t)
            dfs(r,c-1,t)

            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie)

        return res



                

