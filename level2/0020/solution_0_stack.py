"""
    https://leetcode.com/problems/valid-parentheses/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(`LEN`)

    @author: Leon
"""


import collections


class Solution:
    def is_valid(self, s: str) -> bool:
        # not used
        # LEN = len(s)
        stack = collections.deque([])

        DICT = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in DICT:
                top = stack.pop() if stack else '#'

                if DICT[ch] != top:
                    return False
            else:
                stack.append(ch)

        return not stack
