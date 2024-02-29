"""
    https://leetcode.com/problems/valid-palindrome-ii/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        LEN = len(s)
        lo, hi = 0, LEN - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return self.is_palindrome(lo + 1, hi, s) or self.is_palindrome(lo, hi - 1, s)
            lo += 1
            hi -= 1
        return True

    def is_palindrome(self, lo: int, hi: int, s: str) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
