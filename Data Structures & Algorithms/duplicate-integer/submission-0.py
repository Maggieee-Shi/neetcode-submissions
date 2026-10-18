from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic=Counter(nums)
        for k,v in dic.items():
            if v>1:
                return True
        return False