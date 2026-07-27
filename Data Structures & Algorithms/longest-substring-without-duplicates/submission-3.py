class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dup= set()
        maxLen = 0
        for r in range(len(s)):
            while dup and s[r] in dup:
                dup.remove(s[l])
                l+=1
            dup.add(s[r])
            maxLen = max(maxLen,r-l+1)

        return maxLen