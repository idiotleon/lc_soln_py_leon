"""
    https://leetcode.com/problems/hamming-distance/

    Time Complexity:    O(1)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/hamming-distance/editorial/

    @author: Leon
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance
