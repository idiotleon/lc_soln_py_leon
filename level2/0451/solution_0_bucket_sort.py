"""
    https://leetcode.com/problems/sort-characters-by-frequency/

    Time Complexity:    O(`max_freq`) ~ O(`LEN`)
    Space Complexity:   O(`max_freq`) ~ O(`LEN`)

    @author: Leon
"""

import collections


class Solution:
    def frequency_sort(self, s: str) -> str:
        # not used
        # LEN = len(s)

        ch_to_freq = collections.Counter(s)
        max_freq = max(ch_to_freq.values())

        buckets = [[] for _ in range(1 + max_freq)]
        for ch, freq in ch_to_freq.items():
            buckets[freq].append(ch)

        builder = []
        for idx in range(len(buckets) - 1, 0, -1):
            for ch in buckets[idx]:
                builder.append(ch * idx)

        return "".join(builder)
