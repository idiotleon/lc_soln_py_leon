"""
    https://leetcode.com/problems/minimum-depth-of-binary-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    @author: Leon
"""


from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        return self.postorder(root)

    def postorder(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.postorder(node.left)
        right = self.postorder(node.right)

        if left == 0 or right == 0:
            return 1 + max(left, right)
        else:
            return 1 + min(left, right)
