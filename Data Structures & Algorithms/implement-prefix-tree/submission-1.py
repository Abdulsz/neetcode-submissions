class PrefixTree:

    def __init__(self):
        self.trie = {}        

    def insert(self, word: str) -> None:
        trie = self.trie
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
        trie['#'] = True
        


    def search(self, word: str) -> bool:

        trie = self.trie
        for w in word:
            if w not in trie:
                return False

            trie = trie[w]
        return '#' in trie
        

    def startsWith(self, prefix: str) -> bool:

        trie = self.trie
        for p in prefix:
            if p not in trie:
                return False

            trie = trie[p]
        return True
        
        