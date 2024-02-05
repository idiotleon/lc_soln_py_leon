"""
    https://leetcode.com/problems/first-unique-character-in-a-string/

    Time Complexity:    O(`_LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/first-unique-character-in-a-string/editorial/

    @author: Leon
"""

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # not used
        # _LEN = len(s)
        freqs = collections.Counter(s)

        for idx, ch in enumerate(s):
            if freqs[ch] == 1:
                return idx

        return -1
