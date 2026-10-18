class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=0
        # n=len(prices)
        # min_price=[0]*n
        # max_price=[0]*n
        # min_price[0]=prices[0]
        # for i in range(1,n):
        #     min_price[i]=min(min_price[i-1],prices[i])
        # max_price[n-1]=prices[n-1]
        # for i in range(n-2,-1,-1):
        #     max_price[i]=max(max_price[i+1],prices[i])
        # for i in range(n):
        #     max_profit=max(max_profit,(max_price[i]-min_price[i]))

        # return max_profit

        max_profit=0
        min_so_far=float("inf")
        for i in range(len(prices)):
            min_so_far=min(min_so_far,prices[i])
            max_profit=max(max_profit,(prices[i]-min_so_far))
        return max_profit
            