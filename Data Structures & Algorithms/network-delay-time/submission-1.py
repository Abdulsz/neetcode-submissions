class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = {}

        for i in range(1,n+1):
            adj[i] = []

        for u,v,t in times:
            adj[u].append((v,t))

        minHeap = [(0,k)]

        shortest = {}
        while minHeap:

            time,node = heapq.heappop(minHeap)

            if node in shortest:
                continue

            shortest[node] = time

            for nei,t in adj[node]:
                if nei not in shortest:
                    heapq.heappush(minHeap,(t+time,nei))

        
        return max(shortest.values()) if len(shortest) == n else -1
