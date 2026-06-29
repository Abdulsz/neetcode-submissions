class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            
            if stack and stack[-1][0] == i:
                stack[-1][1]+=1
                
                while stack and stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i,1])

        res = []
        for c,n in stack:
            res.append(c*n)

        return "".join(res)

