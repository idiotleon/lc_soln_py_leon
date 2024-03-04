"""
    https://leetcode.com/problems/partition-labels/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/partition-labels/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # not used
        # LEN = len(s)
        last_indices: List[int] = [0] * 26
        for idx, ch in enumerate(s):
            last_indices[ord(ch) - ord('a')] = idx
        lo, hi = 0, 0
        ans = []
        for idx, ch in enumerate(s):
            hi = max(hi, last_indices[ord(ch) - ord('a')])
            if idx == hi:
                len = hi - lo + 1
                ans.append(len)
                lo = hi + 1
        return ans
