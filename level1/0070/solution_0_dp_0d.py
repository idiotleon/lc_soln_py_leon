"""
    https://leetcode.com/problems/climbing-stairs/

    Time Complexity:    O(`n`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def climb_stairs(self, n: int) -> int:
        prev_one, prev_two = 1, 0
        cur = 0
        for _ in range(1, n + 1):
            cur = prev_one + prev_two
            prev_two = prev_one
            prev_one = cur
        return cur
