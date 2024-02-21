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
        shift = 0
        while lo < hi:
            lo = lo >> 1
            hi = hi >> 1
            shift += 1
        return lo << shift
