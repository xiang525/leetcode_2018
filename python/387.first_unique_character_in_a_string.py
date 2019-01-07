"""
use hashtable
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n == 0:
            return -1
        if n == 1:
            return 0
        d = {}
        for letter in s:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for index, value in enumerate(s):
            if d[value] == 1:
                return index
        return -1
