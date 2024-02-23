"""
    https://leetcode.com/problems/diameter-of-binary-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    @author: Leon
"""


from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        (longest, _) = self.postorder(root)
        return longest
        # return self.postorder(root)[0]

    def postorder(self, node: Optional[TreeNode]) -> tuple[int, int]:
        if not node:
            return (0, 0)

        (left_longest, left_path) = self.postorder(node.left)
        (right_longest, right_path) = self.postorder(node.right)

        longest = max(left_longest, right_longest, left_path + right_path)

        return (longest, 1 + max(left_path, right_path))
