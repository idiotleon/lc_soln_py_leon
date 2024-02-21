"""
    https://leetcode.com/problems/bitwise-and-of-numbers-range/

    Time Complexity:    O(1)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/bitwise-and-of-numbers-range/editorial/

    @author: Leon
"""


class Solution:
    def rangeBitwiseAnd(self, lo: int, hi: int) -> int:
        while lo < hi:
            # to turn off the rightmost 1-bit
            hi = hi & (hi - 1)
        return lo & hi
