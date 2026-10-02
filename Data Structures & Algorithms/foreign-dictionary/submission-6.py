class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c:set() for word in words for c in word}

        for i in range(len(words)-1):

            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):

                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

            
        visited = set()
        cycle = set()
        res = []
        def dfs(node):

            if node in cycle:
                return False

            if node in visited:
                return True

            visited.add(node)
            cycle.add(node)
            for nei in adj[node]:

                if not dfs(nei):
                    return False

            cycle.remove(node)
            res.append(node)

            return True


        for key in adj:
            if not dfs(key):
                return ""
            
        return "".join(reversed(res))
