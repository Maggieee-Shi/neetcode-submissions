class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        count=0
        dic={}
        while r<len(s):
            dic[s[r]]=dic.get(s[r],0)+1
            while r-l+1-max(dic.values())>k:
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
            count=max(count,r-l+1)
            r+=1
        return count