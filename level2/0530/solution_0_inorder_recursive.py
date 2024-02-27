"""
    https://leetcode.com/problems/minimum-absolute-difference-in-bst/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    Reference:
    https://leetcode.com/problems/minimum-absolute-difference-in-bst/editorial/

    @author: Leon
"""


from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
        # the minimal distance
        self.ans = 1e9
        # the previous node
        self.prev = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev.val)
            self.prev = node
            inorder(node.right)

        inorder(root)
        return self.ans
