"""
    https://leetcode.com/problems/minimum-window-substring

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

        count = len(t)
        lo = 0
        hi = 0
        shortest = ""

        while hi < len(s):
            if freqs[ord(s[hi])] > 0:
                count -= 1
            freqs[ord(s[hi])] -= 1

            while count == 0:
                if not shortest or hi - lo + 1 < len(shortest):
                    shortest = s[lo:hi + 1]

                if freqs[ord(s[lo])] == 0:
                    count += 1
                freqs[ord(s[lo])] += 1
                lo += 1

            hi += 1
        return shortest
