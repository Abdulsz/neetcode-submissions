class WordDictionary:

    def __init__(self):
        
        self.trie={}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for w in word:
            if w not in trie:
                trie[w] = {}

            trie = trie[w]
        trie['#'] = True

        

    def search(self, word: str) -> bool:
        
        trie = self.trie
        def dfs(t,i):

            if i ==len(word):
                return '#' in t

            if word[i] == '.':
                for c in t:
                    if c != '#' and dfs(t[c],i+1):
                        return True

                return False
            else:
                c = word[i]
                if c in t:
                    if dfs(t[c],i+1):
                        return True
                    
            return False
        return dfs(trie,0)


