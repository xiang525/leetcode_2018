"""
解题思路：
动态规划（Dynamic Programming）

状态转移方程：dp[x + y] += dp[x]

其中dp[x]表示生成数字x的所有可能的组合方式的个数。

https://blog.csdn.net/fuxuemingzhu/article/details/79343825
http://bookshadow.com/weblog/2016/07/25/leetcode-combination-sum-iv/
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for x in range(target + 1):
            for y in nums:
                if x + y <= target:
                    dp[x + y] += dp[x]
        return dp[target]
"""
这个DP的解法不太好理解
"""