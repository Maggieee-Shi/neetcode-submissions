class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            wl=int(s[i:j])
            res.append(s[j+1:j+wl+1])
            i+=(j-i)+1+wl
        return res