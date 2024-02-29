"""
    https://leetcode.com/problems/find-bottom-left-tree-value/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    @author: Leon
"""

from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def find_bottom_left_value(self, root: Optional[TreeNode]) -> int:
        self.deepest = 0
        self.leftmost = root.val

        self.postorder(root, 0)

        return self.leftmost

    def postorder(self, node: Optional[TreeNode], depth: int):
        if not node:
            return

        self.postorder(node.left, 1 + depth)
        self.postorder(node.right, 1 + depth)

        if depth > self.deepest:
            self.deepest = depth
            self.leftmost = node.val
