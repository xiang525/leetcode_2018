
"""
引入辅助数组sells和buys

sells[i]表示在第i天卖出股票所能获得的最大累积收益
buys[i]表示在第i天买入股票所能获得的最大累积收益

初始化令sells[0] = 0，buys[0] = -prices[0]
第i天交易时获得的累计收益只与第i-1天与第i-2天有关

记第i天与第i-1天的价格差：delta = price[i] - price[i - 1]

状态转移方程为：

sells[i] = max(buys[i - 1] + prices[i], sells[i - 1] + delta) 
buys[i] = max(sells[i - 2] - prices[i], buys[i - 1] - delta)
上述方程的含义为：

第i天卖出的最大累积收益 = max(第i-1天买入~第i天卖出的最大累积收益, 第i-1天卖出后反悔~改为第i天卖出的最大累积收益)
第i天买入的最大累积收益 = max(第i-2天卖出~第i天买入的最大累积收益, 第i-1天买入后反悔~改为第i天买入的最大累积收益)
而实际上：

第i-1天卖出后反悔，改为第i天卖出 等价于 第i-1天持有股票，第i天再卖出
第i-1天买入后反悔，改为第i天买入 等价于 第i-1天没有股票，第i天再买入
所求的最大收益为max(sells)。显然，卖出股票时才可能获得收益。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        buys = [0]*n
        sells = [0]*n
        dp = [0] * n
        sells[0] = 0
        buys[0] = -prices[0]
        for i in range(1, n):
            delta = prices[i] - prices[i-1]
            sells[i] = max(buys[i-1] + prices[i], sells[i-1] + delta)
            buys[i] = max(buys[i-1] - delta, sells[i-2] - prices[i])
        return max(sells)
