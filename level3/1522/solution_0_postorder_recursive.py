""""
    https://leetcode.com/problems/diameter-of-n-ary-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(H)

    @author: Leon
"""

from util.other.nary_tree_node import NaryTreeNode


class Solution:
    def diameter(self, root: NaryTreeNode) -> int:
        self.diameter = 0
        self.postorder(root)
        return self.diameter

    def postorder(self, node: NaryTreeNode) -> int:
        deepest = second_deepest = 0
        for child in node.children:
            depth = self.postorder(child)
            if depth > deepest:
                deepest, second_deepest = depth, deepest
            elif depth > second_deepest:
                second_deepest = depth
            self.diameter = max(self.diameter, deepest + second_deepest)
        return deepest + 1
