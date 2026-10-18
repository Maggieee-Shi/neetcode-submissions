class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r=0,0
        count=1
        res=0
        box=set()
        box.add(s[l])
        while r+1<len(s):
            if s[r+1] not in box:
                r+=1
                box.add(s[r])
                count+=1
            else:
                box.remove(s[l])
                l+=1
                res=max(res,count)
                count-=1
        res=max(res,count)

        return res
            
