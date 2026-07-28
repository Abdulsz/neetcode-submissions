class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        arr = list(zip(timestamp,username,website))
        arr.sort()

        users = defaultdict(list)
        patterns = defaultdict(int)
        for time, u,web in arr:
            users[u].append(web)

        for u in users:
            res = set()
            usersites = users[u]

            for i in range(len(usersites)):
                for j in range(i+1,len(usersites)):
                    for k in range(j+1,len(usersites)):
                        res.add((usersites[i],usersites[j],usersites[k]))

            for patt in res:
                patterns[patt]+=1

        
        maxOcc = 0
        maxPatt = tuple()

        for p in patterns:
            cnt = patterns[p]

            if cnt > maxOcc or (cnt == maxOcc and p<maxPatt):
                maxOcc = cnt
                maxPatt = p

        return [maxPatt[0],maxPatt[1],maxPatt[2]]




            

            



