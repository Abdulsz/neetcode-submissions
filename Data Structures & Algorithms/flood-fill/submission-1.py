class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        original = image[sr][sc]

        q = deque([(sr,sc)])
        visited = set()
        if image[sr][sc] == color:
            return image

        while q:
            r,c = q.popleft()

            if image[r][c] == original:
                image[r][c] = color
            
            visited.add((r,c))
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc = dr+r,dc+c
                if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and image[nr][nc] == original: 
                    q.append((nr,nc))
                    #image[nr][nc] = color

        return image