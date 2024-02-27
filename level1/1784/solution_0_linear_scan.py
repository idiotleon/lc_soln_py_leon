"""
    https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def check_ones_segment(self, s: str) -> bool:
        # not used
        # LEN = len(s)
        ZERO, ONE = '0', '1'
        # has any `ZERO` been met
        is_met = False
        for ch in s:
            if ch == ZERO:
                is_met = True
            if ch == ONE:
                if is_met:
                    return False
        return True
