"""
    https://leetcode.com/problems/balanced-binary-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    Reference:
    https://leetcode.com/problems/balanced-binary-tree/editorial/

    @author: Leon
"""


from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return abs(self.get_height(root.left) - self.get_height(root.right)) < 2 and self.is_balanced(root.left) and self.is_balanced(root.right)

    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
