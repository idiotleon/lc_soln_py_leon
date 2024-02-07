"""
    https://leetcode.com/problems/sqrtx/

    Time Complexity:    O(lg(`x`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""


class Solution:
    def my_sqrt(self, x: int) -> int:
        # `lo` has to start with 0,
        # in case `x = 0`
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            # no need to worry about integer overflow in python
            if mid * mid <= x:
                lo = mid
            else:
                hi = mid - 1
        return lo
