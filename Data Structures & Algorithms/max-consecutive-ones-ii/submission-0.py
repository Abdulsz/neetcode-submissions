class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        zeros = 0
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros+=1
            while zeros >1:
                if nums[l] == 0:
                    zeros-=1
                l+=1
            res = max(res, r-l+1)

        return res
            
