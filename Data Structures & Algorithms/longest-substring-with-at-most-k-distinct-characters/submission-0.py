class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        cnt = defaultdict(int)

        res = 0
        l = 0
        for r in range(len(s)):

            c = s[r]
            cnt[c]+=1

            while len(cnt)>k:
                cnt[s[l]]-=1
                if cnt[s[l]] == 0 :
                    del cnt[s[l]]
                
                l+=1
            res = max(res,r-l+1)
        return res
