class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        l,r=0,0
        res=0
        box=set()
        box.add(s[l])
        while r+1<len(s):

            if s[r+1] not in box:
                r+=1
                box.add(s[r])
            else:
                box.remove(s[l])
                l+=1
            res=max(res,r-l+1)
        

        return res
            
