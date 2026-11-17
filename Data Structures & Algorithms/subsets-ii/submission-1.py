class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = []
        res = []

        def dfs(i):

            if i == len(nums):

                res.append(temp.copy())
                return

            temp.append(nums[i])
            dfs(i+1)
            temp.pop()

            j = i
            while j<len(nums)-1 and nums[j]==nums[j+1]:
                j+=1
            dfs(j+1)

        dfs(0)
        return res