class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        count = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):

            c = s[r]
            count[c]+=1
            while len(count) > 2:
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]

                l+=1
            res = max(res,r-l+1)
        return res
            


