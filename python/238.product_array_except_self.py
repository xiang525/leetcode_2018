"""
属于要记住解法的题
我们以一个4个元素的数组为例，nums=[a1,a2,a3,a4]，要想在O(n)的时间内输出结果，比较好的解决方法是提前构造好两个数组：
[1, a1, a1*a2, a1*a2*a3]
[a2*a3*a4, a3*a4, a4, 1]
然后两个数组一一对应相乘，即可得到最终结果 [a2*a3*a4, a1*a3*a4, a1*a2*a4, a1*a2*a3]。
不过，上述方法的空间复杂度为O(n)，可以进一步优化成常数空间，即用一个整数代替第二个数组。
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 1
        n = len(nums)
        res = [1]*n

        for i in range(n-1):
            left *= nums[i]
            res[i+1] *= left

        right = 1
        for i in range(n-1, 0, -1):
            right *= nums[i]
            res[i-1] *= right
        return res
