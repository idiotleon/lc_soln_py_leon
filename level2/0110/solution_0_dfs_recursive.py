"""
    https://leetcode.com/problems/balanced-binary-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    Reference:
    https://leetcode.com/problems/balanced-binary-tree/editorial/

    @author: Leon
"""


from ast import Tuple
from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.dfs(root)
        return is_balanced

    def dfs(self, node: Optional[TreeNode]) -> Tuple[bool, int]:
        if not node:
            return True, -1

        left_is_balanced, left_height = self.dfs(node.left)
        if not left_is_balanced:
            return False, 0

        right_is_balanced, right_height = self.dfs(node.right)
        if not right_is_balanced:
            return False, 0

        return abs(left_height - right_height) < 2, 1 + max(left_height, right_height)
