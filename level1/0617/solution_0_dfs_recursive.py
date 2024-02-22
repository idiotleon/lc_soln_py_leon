"""
    https://leetcode.com/problems/merge-two-binary-trees/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    Reference:
    https://leetcode.com/problems/merge-two-binary-trees/editorial/

    @author: Leon
"""


from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root1, root2)

    def dfs(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node1:
            return node2

        if not node2:
            return node1

        node1.val += node2.val
        node1.left = self.dfs(node1.left, node2.left)
        node1.right = self.dfs(node1.right, node2.right)
        return node1
