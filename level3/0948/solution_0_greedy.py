"""
    https://leetcode.com/problems/bag-of-tokens/

    Time Complexity:    O(`LEN` * lg(`LEN`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/bag-of-tokens/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def bag_of_tokens_score(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        LEN = len(tokens)
        tokens.sort()
        lo, hi = 0, LEN - 1
        most = 0
        score = 0
        while lo <= hi:
            if power >= tokens[lo]:
                power -= tokens[lo]
                lo += 1
                score += 1
                most = max(most, score)
            elif score > 0:
                score -= 1
                power += tokens[hi]
                hi -= 1
            else:
                break
        return most
