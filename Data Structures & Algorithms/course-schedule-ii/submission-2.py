class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = []
        cycle = set()

        courses = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            courses[a].append(b)

        def dfs(c):

            if c in cycle:
                return False

            if c in visited:
                return True

            cycle.add(c)

            for pre in courses[c]:
                if not dfs(pre):
                    return False

            cycle.remove(c)
            visited.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return visited