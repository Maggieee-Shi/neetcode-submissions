class Solution:
    def isValid(self, s: str) -> bool:
        dic={"(":")","{":"}","[":"]"}
        stack=[]
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                temp=stack.pop()
                if dic[temp]!=c:
                    return False
                print(temp)
        if stack:
            return False
        return True