"""
use hashtable
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        n, m = ransomNote, magazine
        if m == 0:
            return False
        for letter in magazine:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for r in ransomNote:
            if r in d and d[r] > 0:  # delete
                d[r] -= 1
            else:
                return False
        return True


"""
use set, count
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
