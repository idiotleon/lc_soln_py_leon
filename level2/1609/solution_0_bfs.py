"""
    https://leetcode.com/problems/even-odd-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(W)

    @author: Leon
"""


import collections
from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        level = 0
        while queue:
            LEN = len(queue)
            for idx in range(LEN):
                cur = queue.popleft()
                value = cur.val

                if level % 2 == 0:
                    if value % 2 == 0:
                        return False

                    if idx < LEN - 1:
                        if value >= queue[0].val:
                            return False

                if level % 2 == 1:
                    if value % 2 == 1:
                        return False

                    if idx < LEN - 1:
                        if value <= queue[0].val:
                            return False

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)
            level += 1
        return True
