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
        lo, hi = 1, x
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid <= x / mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
