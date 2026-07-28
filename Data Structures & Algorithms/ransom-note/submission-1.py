class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magCnt = Counter(magazine)
        ransomCnt = Counter(ransomNote)

        for c in ransomCnt:
            if c not in magCnt or magCnt[c] < ransomCnt[c]:
                return False


        return True