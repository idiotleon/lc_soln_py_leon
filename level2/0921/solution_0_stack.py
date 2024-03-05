"""
    https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # not used
        # LEN = len(s)
        ans = 0
        stk = 0
        for ch in s:
            if ch == '(':
                if stk < 0:
                    ans += abs(stk)
                    stk = 0
                stk += 1
            elif ch == ')':
                stk -= 1
        return ans + abs(stk)
