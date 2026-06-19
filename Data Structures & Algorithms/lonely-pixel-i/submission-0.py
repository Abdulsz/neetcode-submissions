class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        

        rows = [0]*len(picture)
        cols = [0]*len(picture[0])

        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    rows[r]+=1
                    cols[c]+=1
        res = 0
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    if rows[r]>1 or cols[c]>1:
                        continue
                    else:
                        res+=1



        return res

