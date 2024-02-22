"""
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

    Time Complexity:    O((`LEN1` + `LEN2`) * average_length_word) ~ O(max(`LEN1`, LEN2) * average_length_word)
    Space Complexity:   O((`LEN1` + `LEN2`) * average_length_word) ~ O(max(`LEN1`, LEN2) * average_length_word)

    Reference:
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/editorial/comments/1658722
    https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def array_strings_are_equal(self, words1: List[str], words2: List[str]) -> bool:
        # not used
        # LEN1, LEN2 = len(words1), len(words2)
        return "".join(words1) == "".join(words2)
