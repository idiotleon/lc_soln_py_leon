"""
    https://leetcode.com/problems/balance-a-binary-search-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    Reference:
    https://leetcode.com/problems/balance-a-binary-search-tree/solutions/540038/python-3-easy-to-understand/comments/480141
    https://leetcode.com/problems/balance-a-binary-search-tree/solutions/540038/python-3-easy-to-understand/

    @author: Leon
"""

from ast import List
from typing import Optional
from util.tree.tree_node import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.nodes: List[TreeNode] = []
        self.inorder(root)
        LEN = len(self.nodes)
        return self.build(0, LEN - 1)

    def build(self, lo: int, hi: int) -> TreeNode:
        if lo > hi:
            return
        mid = lo + (hi - lo) // 2
        root = self.nodes[mid]
        root.left = self.build(lo, mid - 1)
        root.right = self.build(mid + 1, hi)
        return root

    def inorder(self, node: Optional[TreeNode]):
        if not node:
            return
        self.inorder(node.left)
        self.nodes.append(node)
        self.inorder(node.right)
