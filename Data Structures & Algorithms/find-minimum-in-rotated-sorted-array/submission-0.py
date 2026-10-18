class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # min is to the right of mid
                l = mid + 1
            else:
                # min is at mid or to the left of mid
                r = mid
        return nums[l]