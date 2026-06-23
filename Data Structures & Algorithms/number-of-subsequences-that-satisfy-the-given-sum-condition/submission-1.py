class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r=len(nums)-1   
        cnt = 0
        MOD = 10**9+7
        
        while l<=r:

            while l<=r and nums[l] + nums[r] > target:
                r-=1
            if l<=r:
                cnt = (cnt+pow(2,r-l,MOD))%MOD
            l+=1

        return cnt