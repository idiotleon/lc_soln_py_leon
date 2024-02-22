"""
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

    Time Complexity:    O((`LEN1` + `LEN2`) * average_length_word) ~ O(max(`LEN1`, LEN2) * average_length_word)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def array_strings_are_equal(self, words1: List[str], words2: List[str]) -> bool:
        LEN1, LEN2 = len(words1), len(words2)
        idx1, idx2 = 0, 0
        idx_ch1, idx_ch2 = 0, 0
        while idx1 < LEN1 and idx2 < LEN2:
            WORD1, WORD2 = words1[idx1], words2[idx2]
            CH1, CH2 = WORD1[idx_ch1], WORD2[idx_ch2]
            if CH1 != CH2:
                return False
            LEN_WORD1, LEN_WORD2 = len(WORD1), len(WORD2)
            idx_ch1 += 1
            idx_ch2 += 1
            if idx_ch1 == LEN_WORD1:
                idx1 += 1
                idx_ch1 = 0
            if idx_ch2 == LEN_WORD2:
                idx2 += 1
                idx_ch2 = 0
        return idx1 == LEN1 and idx2 == LEN2
