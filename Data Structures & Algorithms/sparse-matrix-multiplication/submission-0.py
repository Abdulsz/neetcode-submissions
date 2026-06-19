class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        row1 = len(mat1)
        col1 = len(mat1[0])

        row2 = len(mat2)
        col2 = len(mat2[0])

        res = [[0]*col2 for _ in range(row1)]
        for i in range(row1):
            for j in range(col2):
                for x in range(col1):
                    res[i][j] += mat1[i][x] * mat2[x][j]

        return res

