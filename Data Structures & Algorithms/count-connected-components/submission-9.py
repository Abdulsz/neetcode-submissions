class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        connected = 0
        visited = set()
        def dfs(node,prev):
            if node in visited:
                return 

            visited.add(node)

            for nei in adj[node]:
                
                dfs(nei,node)

        for i in range(n):
            if i not in visited:
                connected+=1
                dfs(i,-1)

        return connected

        
