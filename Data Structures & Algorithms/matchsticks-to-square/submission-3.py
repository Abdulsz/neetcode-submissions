class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        res = [0]*4
        total = sum(matchsticks)
        side = total//4

        matchsticks.sort(reverse=True)

        if total%4!=0:
            return False

        def backtrack(i):

            if i == len(matchsticks):
                return True

            for j in range(len(res)):
                if matchsticks[i]+res[j] <= side:
                    res[j] += matchsticks[i]
                
                    if backtrack(i+1):
                        return True
                    res[j]-=matchsticks[i]
            return False

        return backtrack(0)
                    
                    





                
                