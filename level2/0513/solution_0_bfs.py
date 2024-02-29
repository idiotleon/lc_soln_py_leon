"""
    https://leetcode.com/problems/find-bottom-left-tree-value/

    Time Complexity:    O(N)
    Space Complexity:   O(W)

    @author: Leon
"""


import collections
from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def find_bottom_left_value(self, root: Optional[TreeNode]) -> int:
        queue = collections.queue([])
        queue.append(root)
        ans = None
        while queue:
            LEN = len(queue)
            for i in range(LEN):
                cur = queue.popleft()
                if i == 0:
                    ans = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return ans
