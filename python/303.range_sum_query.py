"""
Online explanation: http://www.cnblogs.com/grandyang/p/4952464.html
not easy to do by myself, need more practice.
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        n = len(nums)
        for i in range(1, n):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - (self.dp[i - 1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)