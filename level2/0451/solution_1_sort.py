"""
    https://leetcode.com/problems/sort-characters-by-frequency/

    Time Complexity:    O(`LEN` * lg(`LEN`))
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def frequency_sort(self, s: str) -> str:
        if not s:
            return ""

        # not used
        # LEN = len(s)

        freqs: List[int] = [0] * 128
        for ch in s:
            freqs[ord(ch)] += 1

        chs = [*s]

        chs.sort(key=lambda ch: (freqs[ord(ch)], ch), reverse=True)

        return "".join(chs)
