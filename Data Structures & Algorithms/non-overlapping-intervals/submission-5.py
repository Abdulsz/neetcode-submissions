class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort()
        cnt = 0
        prev = intervals[0][1]
        for i,(start,end) in enumerate(intervals[1:]):
            
            if start<prev:
                prev = min(prev,end)
                cnt+=1
            else:
                prev = end

        return cnt
        
            
                
            