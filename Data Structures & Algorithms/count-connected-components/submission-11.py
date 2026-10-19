class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for a,b, in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node,prev):

            visited.add(node)

            for nei in adj[node]:
                if nei != prev and nei not in visited:
                    dfs(nei,node)

        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt+=1
                dfs(i,-1)

        return cnt

