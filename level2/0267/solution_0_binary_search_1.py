"""
    https://leetcode.com/problems/valid-perfect-square/

    Time Complexity:    O(lg(`num`))
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        lo, hi = 0, num // 2
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            square = mid * mid
            if square == num:
                return True
            if square > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
