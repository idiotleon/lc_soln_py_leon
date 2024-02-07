"""
    https://leetcode.com/problems/guess-number-higher-or-lower/

    Time Complexity:    O(lg(`n`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/
    
    @author: Leon
"""


def guess(num: int) -> int:
    # the dummy API
    return 0


class Solution:
    def guess_number(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if guess(mid) == 0:
                return mid
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
