class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(i,path,total):
            if total==target:
                res.append(path.copy())
                return
            if total>target or i>=len(nums):
                return
           
            path.append(nums[i])
            helper(i,path,total+nums[i])
            path.pop()
            helper(i+1,path,total)
        helper(0,[],0)
        return res