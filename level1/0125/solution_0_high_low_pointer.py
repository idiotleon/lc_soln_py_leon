"""
    https://leetcode.com/problems/valid-palindrome/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        LEN = len(s)
        lo, hi = 0, LEN - 1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
