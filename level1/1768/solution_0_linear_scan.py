"""
    https://leetcode.com/problems/merge-strings-alternately/

    Time Complexity:    O(`LEN1` + `LEN2`) ~ O(max(`LEN1`, `LEN2`))
    Space Complexity:   O(1)

    @author: Leon
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        LEN1, LEN2 = len(word1), len(word2)
        idx1, idx2 = 0, 0
        ans = []
        while idx1 < LEN1 or idx2 < LEN2:
            if idx1 < LEN1:
                ans.append(word1[idx1])
            if idx2 < LEN2:
                ans.append(word2[idx2])
            idx1 += 1
            idx2 += 1
        return "".join(ans)
