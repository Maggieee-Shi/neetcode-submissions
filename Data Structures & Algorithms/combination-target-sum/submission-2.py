class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(i,target,sol):
            if target==0:
                res.append(sol.copy())
                return
            if target<0 or i>=len(nums):
                return
            sol.append(nums[i])
            helper(i,target-nums[i],sol)
            sol.pop()
            helper(i+1,target,sol)
        helper(0,target,[])
        return res