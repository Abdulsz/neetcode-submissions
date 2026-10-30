class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        

        cnt = 0
        nums.sort()

        for i in range(len(nums)):

            j = i+1
            k = len(nums)-1

            while j<k:
                res = nums[i]+nums[j]+nums[k]
                if res<target:
                    cnt+=k-j
                    j+=1

                else:
                    k-=1

        return cnt
                

                
