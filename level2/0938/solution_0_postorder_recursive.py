"""
    https://leetcode.com/problems/range-sum-of-bst/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    Reference:
    https://leetcode.com/problems/range-sum-of-bst/editorial/

    @author: Leon
"""


from typing import Optional
from util.tree.tree_node import TreeNode


class Solution:
    def range_sum_BST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(low, high, root)

    def dfs(self, low: int, high: int, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        sum = 0
        value = node.value

        if value >= low:
            sum += self.dfs(low, high, node.left)

        if value <= high:
            sum += self.dfs(low, high, node.right)

        if value in range(low, high + 1):
            sum += value

        return sum
