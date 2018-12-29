# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        numRoom = available = 0
        i = 0
        for start in starts:
            while ends[i] <= start:
                available += 1
                i += 1
            if available:
                available -= 1
            else:
                numRoom += 1
        return numRoom


"""
use min heap O(nlogn)
一种使用最小堆来解题的方法，这种方法先把所有的时间区间按照起始时间排序，然后新建一个最小堆，开始遍历时间区间，如果堆不为空，且首元素小于等于当前区间的起始时间，
我们去掉堆中的首元素，把当前区间的结束时间压入堆，由于最小堆是小的在前面，那么假如首元素小于等于起始时间，说明上一个会议已经结束，可以用该会议室开始下一个会议了，
所以不用分配新的会议室，遍历完成后堆中元素的个数即为需要的会议室的个数，
"""
import heapq
def minMeetingRooms(self, intervals):
    intervals.sort(key=lambda x: x.start)
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i.start >= heap[0]:
            # means two intervals can use the same room
            heapq.heapreplace(heap, i.end)
        else:
            # a new room is allocated
            heapq.heappush(heap, i.end)
    return len(heap)
