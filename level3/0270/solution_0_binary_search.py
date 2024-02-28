"""
    https://leetcode.com/problems/closest-binary-search-tree-value/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    @author: Leon
"""


from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        while root:
            if abs(root.val - target) < abs(ans - target):
                ans = root.val
            elif abs(root.val - target) == abs(ans - target):
                ans = min(ans, root.val)

            if root.val < target:
                root = root.right
            else:
                root = root.left
        return ans
