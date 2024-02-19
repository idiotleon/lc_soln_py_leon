"""
    https://leetcode.com/problems/power-of-two/

    Time Complexity:    O(lg(`n`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/power-of-two/editorial/

    @author: Leon
"""


class Solution:
    def is_power_of_two(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
