class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        globalMin = arrays[0][0]
        globalMax = arrays[0][-1] 
        res = float('-inf')
        for i in range(1,len(arrays)):
            currMin = arrays[i][0]
            currMax = arrays[i][-1]

            res = max(res, currMax - globalMin, globalMax-currMin)
            globalMax = max(currMax,globalMax)
            globalMin = min(globalMin,currMin)

        return res

