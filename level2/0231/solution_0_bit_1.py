"""
    https://leetcode.com/problems/power-of-two/

    Time Complexity:    O(1)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/power-of-two/editorial/

    @author: Leon
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0
