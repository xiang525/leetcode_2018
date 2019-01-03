"""
O(nk) is not the best solution
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
    	if k > len(nums) or nums == []: return []
    	res = []
    	for i in range(len(nums)+1-k):
    		window = nums[i:i+k]
    		res.append(max(window))
    	return res

if __name__ == '__main__':
	a = Solution()
	print a.maxSlidingWindow([1],1)


# 我自己做的很直白的思想， 最好看下别人的solution

"""
 jiuzhong solution， discussion codes
 O(n);双端队列
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []; deque = []
        for index, value in enumerate(nums):
            if deque and deque[0] + k <= index: # out of window so need to remove the first element in the deque
                deque.pop(0)
            while deque and nums[deque[-1]] < value:
                deque.pop()
            deque.append(index)
            if index+1 >= k: # when arrives the k element in the window, maxvalue needs to be stored in ans
                ans.append(nums[deque[0]]) # deque[0] stores the max value in the window
        return ans




