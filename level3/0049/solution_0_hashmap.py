"""
    https://leetcode.com/problems/group-anagrams/

    Time Complexity:    O(`LEN` * avg_len_word)
    Space Complexity:   O(`LEN` * avg_len_word)

    @author: Leon
"""

from ast import List
import collections


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        # not used
        # LEN = len(strs)
        bitmask_to_words = collections.defaultdict(list)
        for s in strs:
            freqs = [0] * 26
            for ch in s:
                freqs[ord(ch) - ord('a')] += 1
            bitmask_to_words[tuple(freqs)].append(s)
        return bitmask_to_words.values()
