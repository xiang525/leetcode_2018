"""
倒过来想，一个数 * 2 就是把它的二进制全部左移一位，也就是说 1的个数是相等的。
那么我们可以利用这个结论来做。res[i /2] 然后看看最低位是否为1即可（上面*2一定是偶数，
这边比如15和14除以2都是7，但是15时通过7左移一位并且+1得到，14则是直接左移）
所以res[i] = res[i >>1] + (i&1).
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0] * (num + 1)
        for i in range(1, num+1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


