class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = r= 0
        maxLen = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            while (r-l+1) * nums[r] > total+k:
                total-=nums[l]
                l+=1

            maxLen = max(maxLen,r-l+1)

        return maxLen


    

            
