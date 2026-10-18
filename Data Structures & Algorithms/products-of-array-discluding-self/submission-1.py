class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix_p=[0]*(n)
        prefix_p[0]=1
        for i in range(n-1):
            prefix_p[i+1]=prefix_p[i]*nums[i]
        sufix_p=[0]*n
        sufix_p[n-1]=1
        for i in range(n-1,0,-1):
            sufix_p[i-1]=sufix_p[i]*nums[i]
            print(sufix_p[i-1],i)
        res=[0]*n
        for i in range(n):
            res[i]=prefix_p[i]*sufix_p[i]
        return res