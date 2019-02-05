class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        i=j=0
        m,n = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                i +=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res