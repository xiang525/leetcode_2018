class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        max_diff = -100
        print (nums)
        for i in range(0, n-1):
            diff = abs(nums[i] - nums[i+1])
            print (diff)
            print (diff, max_diff)
            max_diff = max(max_diff, diff)
        return max_diff




a = Solution()
nums = [1, 10000000]
print (a.maximumGap(nums))

