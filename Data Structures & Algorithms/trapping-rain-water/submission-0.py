class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_high=[0]*n
        right_high=[0]*n
        for i in range(n-1):
            left_high[i+1]=max(left_high[i],height[i])
        for i in range(n-1,0,-1):
            right_high[i-1]=max(right_high[i],height[i])
        print(left_high,right_high)
        area=0
        for i in range(n):
            area+=(max(0,min(left_high[i],right_high[i])-height[i]))
            print(area)
        return area