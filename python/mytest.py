class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {}
        n = len(A)
        for i in range(n):
            for j in range(n):
                if A[i] == B[j]:
                    d[i] = j
        return d




a = Solution()
A = [12,28,46,32,50]
B = [50,12,32,46,28]
d = a.anagramMappings(A, B)
print (d)
