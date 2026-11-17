class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def dfs(opened,closed):

            if opened == closed == n:
                res.append("".join(temp))
                return

            if opened <n:
                temp.append('(')
                dfs(opened+1,closed)
                temp.pop()

            if opened>closed:
                temp.append(')')
                dfs(opened,closed+1)
                temp.pop()

        dfs(0,0)
        return res
            





