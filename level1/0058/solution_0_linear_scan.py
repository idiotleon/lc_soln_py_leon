"""
    https://leetcode.com/problems/length-of-last-word/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        LEN = len(s)
        SPACE = ' '
        idx = LEN - 1
        # the running length
        running = 0
        # has any non space character been met
        is_met: bool = False
        for idx in reversed(range(LEN)):
            CH = s[idx]
            if CH == SPACE:
                if is_met:
                    return running
            else:
                is_met = True
                running += 1

        return running
