class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(int)
        for i,num in enumerate(nums):
            dic[num]=i
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in dic and dic[complement]!=i:
                return [i,dic[complement]]
