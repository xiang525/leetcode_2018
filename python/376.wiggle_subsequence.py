"""
O(n)非常巧妙的greedy解法,利用两个辅助pointer inc, dec分别保存当前状态为递增/递减的子序列的最大长度。
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        q = 1
        n = len(nums)
        for i in range(1, n):
            if (nums[i] > nums[i - 1]):
                p = q + 1
            elif (nums[i] < nums[i - 1]):
                q = p + 1

        return min(n, max(p, q))
