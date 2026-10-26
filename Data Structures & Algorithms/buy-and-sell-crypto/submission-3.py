class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        less=prices[0]
        maxi=0
        for i in range(1,len(prices)):
            if prices[i]<less:
                less=prices[i]
            else:
                profit=prices[i]-less
                if profit>maxi:
                    maxi=profit
        return maxi