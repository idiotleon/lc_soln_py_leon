"""
    https://leetcode.com/problems/sort-characters-by-frequency/

    Time Complexity:    O(`max_freq`)
    Space Complexity:   O(`max_freq`)

    @author: Leon
"""

import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s

        ch_to_freqs = collections.Counter(s)
        max_freq = max(ch_to_freqs.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for ch, freq in ch_to_freqs.items():
            buckets[freq].append(ch)

        builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for ch in buckets[i]:
                builder.append(ch * i)

        return "".join(builder)
