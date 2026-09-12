class Union:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        self.rank = [1]*(n+1)

    def find(self,x):

        while x != self.par[x]:
            self.par[x] = self.find(self.par[x])
            x = self.par[x]
        return x

    def union(self,a,b):

        par1 = self.find(a)
        par2 = self.find(b)

        if par1 == par2:
            return False

        if self.rank[par1]>self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1]+= self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uFind = Union(len(edges))

        for a,b in edges:

            if not uFind.union(a,b):
                return [a,b]

        
        