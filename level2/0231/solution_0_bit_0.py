"""
    https://leetcode.com/problems/power-of-two/

    Time Complexity:    O(1)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/power-of-two/editorial/

    @author: Leon
"""


class Solution:
    def is_power_of_two(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n
