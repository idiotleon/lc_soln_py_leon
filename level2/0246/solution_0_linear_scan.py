"""
    https://leetcode.com/problems/strobogrammatic-number/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def isStrobogrammatic(self, s: str) -> bool:
        DICT = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        LEN = len(s)
        lo, hi = 0, LEN - 1
        while lo <= hi:
            if s[lo] not in DICT or DICT[s[lo]] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
