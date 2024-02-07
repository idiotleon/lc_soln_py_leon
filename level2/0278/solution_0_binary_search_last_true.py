"""
    https://leetcode.com/problems/first-bad-version/

    Time Complexity:    O(lg(`n`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""


from random import randint


def is_bad_version(version: int) -> bool:
    # dummy API
    return version == randint()


class Solution:
    def first_bad_version(self, n: int) -> int:
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if not is_bad_version(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo + 1
