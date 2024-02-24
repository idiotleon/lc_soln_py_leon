"""
    https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(`LEN`) / O(1)

    @author: Leon
"""


class Solution:
    def remove_duplicates(self, s: str) -> str:
        # not used
        # LEN = len(s)
        ans = []
        for ch in s:
            if ans and ans[-1] == ch:
                ans.pop()
            else:
                ans.append(ch)
        return "".join(ans)
