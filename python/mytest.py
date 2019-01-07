class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        n = len(haystack)
        m = len(needle)
        i = 0
        while i+m-1 < n:
           
            if haystack[i] == needle[0] and ''.join(haystack[i:i+m]) == needle:                
                return i
            else:
                i += 1

        return -1




a = Solution()
haystack = "hello"
needle = "ll"
a.strStr(haystack, needle)
