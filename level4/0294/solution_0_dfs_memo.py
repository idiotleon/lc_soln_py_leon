"""
    https://leetcode.com/problems/flip-game-ii/

    Time Complexity:    O(`LEN` ^ 2)
    Space Complexity:   O(`LEN` ^ 2)

    Reference:
        https://leetcode.com/problems/flip-game-ii/solutions/1045653/python3-dp/

    @author: Leon
"""

from functools import cache


class Solution:
    def canWin(self, current: str) -> bool:
        @cache
        def can_win(s):
            if "++" not in s:
                return False
            LEN = len(s)
            for i in range(LEN - 1):
                if s[i:i+2] == "++" and not can_win(s[:i] + "--" + s[i+2:]):
                    return True
            return False
        return can_win(current)
