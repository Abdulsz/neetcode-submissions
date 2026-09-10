class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)

        preReq = {}

        def dfs(course):
            if course not in preReq:
                preReq[course] = set()
                for pre in adj[course]:
                    preReq[course] |= dfs(pre)

                preReq[course].add(course)
            return preReq[course]

                
        for i in range(numCourses):
            dfs(i)

        res = []
        for a,b in queries:
            res.append(a in preReq[b])

        return res