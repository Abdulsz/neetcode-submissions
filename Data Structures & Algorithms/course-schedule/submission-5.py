class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            courses[a].append(b)

        visited = set()

        def dfs(course):

            if course in visited:
                return False

            if courses[course] == []:
                return True

            visited.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False

            courses[course] = []
            visited.remove(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False


        return True