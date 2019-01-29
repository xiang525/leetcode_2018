"""
记忆化搜索（DFS + Memoization）

记当前房间为root，如果偷窃当前房间，则其左右孩子left和right均不能偷窃；而其4个孙子节点（ll，lr，rl，rr）不受影响。

因此最大收益为：

maxBenifit = max(rob(left) + rob(right), root.val + rob(ll) + rob(lr) + rob(rl) + rob(rr))
使用字典valMap记录每一个访问过的节点，可以避免重复运算。
"""
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        valMap = dict()
        def solve(root, path):
            if root is None: return 0
            if path not in valMap:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:  ll, lr = left.left, left.right
                if right: rl, rr = right.left, right.right
                passup = solve(left, path + 'l') + solve(right, path + 'r')
                grabit = root.val + solve(ll, path + 'll') + solve(lr, path + 'lr') \
                         + solve(rl, path + 'rl') + solve(rr, path + 'rr')
                valMap[path] = max(passup, grabit)
            return valMap[path]
        return solve(root, '')