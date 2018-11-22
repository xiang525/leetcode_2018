import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: return 0
        opt = [0 for i in range(n)]
        opt[0] = 0
        minvalue = prices[0]
        for i in range(1, n):
            minvalue = min(minvalue, prices[i])
            if prices[i] < opt[i-1]:
                opt[i] = prices[i]
            else:
                print(prices[i], minvalue)
                opt[i] = max(prices[i] - minvalue, opt[i-1])
            print(opt)
        return max(opt)




a = Solution()
prices = [1,2]
value = a.maxProfit(prices)
print(value)
