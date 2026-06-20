class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        row1 = set(mat[0])
        for r in mat[1:]:
            tmp = set()
            for c in r:
                if c in row1:
                    tmp.add(c)
            row1 = tmp
        return min(row1) if row1 else -1