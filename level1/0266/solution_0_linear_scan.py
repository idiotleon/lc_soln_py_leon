"""
    https://leetcode.com/problems/palindrome-permutation/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # not used
        # LEN = len(s)
        freqs = [0] * 26
        for ch in s:
            freqs[ord(ch) - ord('a')] += 1
        count = 0
        for freq in freqs:
            if freq % 2 == 1:
                count += 1
        return count < 2
