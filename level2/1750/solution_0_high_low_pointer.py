"""
    https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/editorial/

    @author: Leon
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        LEN = len(s)
        lo, hi = 0, LEN - 1
        while lo < hi:
            ch = s[lo]
            if ch != s[hi]:
                break
            while lo <= hi and s[lo] == ch:
                lo += 1
            while lo <= hi and s[hi] == ch:
                hi -= 1
        return hi - lo + 1
