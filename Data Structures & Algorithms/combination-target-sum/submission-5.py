class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        temp = []
        res = []

        def combSum(i,cur):

            if cur>target or i==len(nums):
                return

            if cur == target:
                res.append(temp.copy())
                return

            temp.append(nums[i])
            combSum(i,cur+nums[i])
            temp.pop()
            combSum(i+1,cur)


        combSum(0,0)
        return res