"""
    https://leetcode.com/problems/range-sum-of-bst/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    Reference:
    https://leetcode.com/problems/range-sum-of-bst/editorial/s

    @author: Leon
"""


from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def range_sum_BST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                value = node.value
                if low <= value <= high:
                    ans += value
                if low < value:
                    stack.append(node.left)
                if value < high:
                    stack.append(node.right)
        return ans
