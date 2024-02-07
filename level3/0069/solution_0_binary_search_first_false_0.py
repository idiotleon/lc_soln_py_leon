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
        # sanity check required,
        # if `lo` starts with 0
        if x == 0:
            return 0

        # the search range needs to be enlarged,
        # in order to find the next/1st false element.
        # e.g. x = 1
        lo, hi = 0, x + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid <= x / mid:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
