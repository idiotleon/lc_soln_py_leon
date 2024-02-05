"""
    https://leetcode.com/problems/minimum-window-substring

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
        https://leetcode.com/problems/minimum-window-substring/solutions/4673541/beats-100-explained-any-language-by-prodonik/

    @author: Leon
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        freqs = [0] * 128
        for ch in t:
            freqs[ord(ch)] += 1

        LEN = len(s)
        count = len(t)
        lo = 0
        hi = 0
        lo_ans = 0
        shortest = LEN

        while hi < len(s):
            if freqs[ord(s[hi])] > 0:
                count -= 1
            freqs[ord(s[hi])] -= 1

            while count == 0:
                if not shortest or hi - lo < shortest:
                    shortest = hi - lo
                    lo_ans = lo

                if freqs[ord(s[lo])] == 0:
                    count += 1
                freqs[ord(s[lo])] += 1
                lo += 1

            hi += 1
        return "" if shortest == LEN else s[lo_ans: lo_ans + shortest + 1]
