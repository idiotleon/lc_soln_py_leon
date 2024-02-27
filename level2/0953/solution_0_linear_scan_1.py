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
    def is_alien_sorted(self, words: List[str], order: str) -> bool:
        LEN_WORDS = len(words)

        ch_to_idx = {}
        for (idx, ch) in enumerate(order):
            ch_to_idx[ch] = idx

        # index of the word
        for idx_w in range(LEN_WORDS - 1):
            WORD_CUR, WORD_NEXT = words[idx_w], words[1 + idx_w]
            LEN_CUR, LEN_NEXT = len(WORD_CUR), len(WORD_NEXT)
            # index of the char
            for idx_ch in range(LEN_CUR):
                if idx_ch >= LEN_NEXT:
                    return False
                if WORD_CUR[idx_ch] != WORD_NEXT[idx_ch]:
                    if ch_to_idx[WORD_CUR[idx_ch]] > ch_to_idx[WORD_NEXT[idx_ch]]:
                        return False
                    break
        return True
