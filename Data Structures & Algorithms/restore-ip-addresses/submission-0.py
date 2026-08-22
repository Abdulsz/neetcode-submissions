class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        temp = []

        def dfs(i):
            
            if len(temp) == 4:
                if i == len(s):
                    res.append(".".join(temp))
                return

            if len(temp)>=4:
                return

            for j in range(i, min(i+3,len(s))):
                
                val = int(s[i:j+1])
                if val <=255:

                    curr = s[i:j+1]
                    if len(curr)>1 and curr[0] == "0":
                        continue
                    temp.append(curr)
                
                    dfs(j+1)

                    temp.pop()
        
        dfs(0)
        return res


            
