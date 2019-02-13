"""
解法I 深度优先搜索（DFS）：

从出发机场开始，按照到达机场的字典序递归搜索

在搜索过程中删除已经访问过的机票

将到达机场分为两类：子行程中包含出发机场的记为left，不含出发机场的记为right

返回时left排在right之前，详见代码。
"""

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        routes = collections.defaultdict(list)
        for s, e in tickets:
            routes[s].append(e)
        def solve(start):
            left, right = [], []
            for end in sorted(routes[start]):
                if end not in routes[start]:
                    continue
                routes[start].remove(end)
                subroutes = solve(end)
                if start in subroutes:
                    left += subroutes
                else:
                    right += subroutes
            return [start] + left + right
        return solve("JFK")



"""
解法II 欧拉通路（Eulerian path）：

参考链接：https://leetcode.com/discuss/84659/short-ruby-python-java-c

将机场视为顶点，机票看做有向边，可以构成一个有向图。

通过图（无向图或有向图）中所有边且每边仅通过一次的通路称为欧拉通路，相应的回路称为欧拉回路。具有欧拉回路的图称为欧拉图（Euler Graph），具有欧拉通路而无欧拉回路的图称为半欧拉图。

因此题目的实质就是从JFK顶点出发寻找欧拉通路，可以利用Hierholzer算法。
"""
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]