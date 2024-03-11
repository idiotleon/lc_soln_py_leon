"""
    https://leetcode.com/problems/custom-sort-string/

    Time Complexity:    O(`L`)
    Space Complexity:   O(`L`)

    @author: Leon
"""


from ast import List


class Solution:
    def custom_sort_string(self, order: str, s: str) -> str:
        ch_to_freq = {}
        for ch in s:
            ch_to_freq[ch] = 1 + ch_to_freq.get(ch, 0)

        ans: List[str] = []
        for ch in order:
            while ch_to_freq.get(ch, 0) > 0:
                ans.append(ch)
                ch_to_freq[ch] -= 1

        for ch, freq in ch_to_freq.items():
            while freq > 0:
                ans.append(ch)
                freq -= 1

        return "".join(ans)
