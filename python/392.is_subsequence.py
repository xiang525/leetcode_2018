"""
解题思路：利用队列（Queue）数据结构。
将s加入队列，遍历t，当t的当前字符c与队头相同时，将队头弹出。
最后判断队列是否为空即可。
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queue = collections.deque(s)
        for c in t:
            if not queue: return True # if no check: IndexError: deque index out of range
            if c == queue[0]:
                queue.popleft()
        return not queue