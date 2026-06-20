class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(board)
        COLS = len(board[0])
        while True:
                
            crush = set()
            
            for r in range(ROWS):
                for c in range(COLS-2):
                    if board[r][c] != 0 and board[r][c] == board[r][c+1] == board[r][c+2]:
                        crush.add((r,c))
                        crush.add((r,c+1))
                        crush.add((r,c+2))

                    
            for c in range(COLS):
                for r in range(ROWS-2):
                    if board[r][c] != 0 and board[r][c] == board[r+1][c] == board[r+2][c]:
                        crush.add((r,c))
                        crush.add((r+1,c))
                        crush.add((r+2,c))
            if not crush:
                return board

            for r,c in crush:
                board[r][c] = 0

            for c in range(COLS):
                ptr = ROWS-1
                for r in range(ROWS-1,-1,-1):
                    if board[r][c] != 0:
                        board[ptr][c] = board[r][c]
                        ptr-=1
                    
                while ptr>=0:
                    board[ptr][c] =0
                    ptr-=1

        return board

