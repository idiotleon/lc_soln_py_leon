"""
    https://leetcode.com/problems/average-of-levels-in-binary-tree/

    Time Complexity:    O(N)
    Space Complexity:   O(W)

    @author: Leon
"""


from ast import List
from collections import deque
from typing import Optional

from util.tree.tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0.0]
        dq = deque([root])
        ans = []
        while dq:
            LEN = len(dq)
            sum = 0
            for _ in range(LEN):
                cur = dq.popleft()
                sum += cur.val
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            average = sum / LEN
            ans.append(average)
        return ans
