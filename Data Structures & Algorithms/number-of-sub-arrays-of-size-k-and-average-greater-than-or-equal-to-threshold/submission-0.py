class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = 0
        curSum = 0
        l = 0

        for r in range(k):
            curSum += arr[r]

        if curSum/k >= threshold:
            res+=1

        for r in range(k,len(arr)):

            curSum += arr[r]
            curSum-=arr[l]
            l+=1
            if curSum/k >= threshold:
                res+=1

        return res


