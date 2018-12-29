class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        if n == 0:
            return ans
        start = 0
        
        while start <= n-k:
            end = start + k
            print(start, end)
            max_value = max(nums[start:end])
            print (max_value)
            ans.append(max_value)
            start += 1
        return ans




a = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(a.maxSlidingWindow(nums, k))

