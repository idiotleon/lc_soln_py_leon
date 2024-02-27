"""
    https://leetcode.com/problems/verifying-an-alien-dictionary/

    Time Complexity:    O(`LEN_WORDS` * average_length_word)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/verifying-an-alien-dictionary/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        LEN_WORDS = len(words)
        self.ch_to_idx = {ch: idx for idx, ch in enumerate(order)}
        for idx in range(LEN_WORDS - 1):
            if self.is_bigger(words[idx], words[idx + 1]):
                return False
        return True

    def is_bigger(self, prev: str, cur: str) -> bool:
        LEN_PREV, LEN_CUR = len(prev), len(cur)
        for ch_p, ch_c in zip(prev, cur):
            idx_p, idx_c = self.ch_to_idx[ch_p], self.ch_to_idx[ch_c]
            if idx_p != idx_c:
                return idx_p > idx_c
        return LEN_PREV > LEN_CUR
