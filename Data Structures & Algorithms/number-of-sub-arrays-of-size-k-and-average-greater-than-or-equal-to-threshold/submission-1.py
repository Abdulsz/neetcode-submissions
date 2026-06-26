class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = 0
        cnt = 0

        for i in range(k):
            curSum+=arr[i]

        if curSum/k >= threshold:
            cnt+=1

        l = 0
        for r in range(k,len(arr)):

            curSum += arr[r]
            curSum -= arr[l]
            l+=1

            if curSum/k>=threshold:
                cnt+=1

        return cnt


        