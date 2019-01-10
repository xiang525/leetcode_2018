import collections
class Solution(object):
    def leastInterval(self, tasks, N):
        task_counts = collections.Counter(tasks).values()
        print(task_counts)
        M = max(task_counts)
        print(M)
        Mct = task_counts.count(M)
        print(Mct)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)
        


a = Solution()
tasks = ["A","A","A","B","B","B","C"]; n = 2
a.leastInterval(tasks, n)

