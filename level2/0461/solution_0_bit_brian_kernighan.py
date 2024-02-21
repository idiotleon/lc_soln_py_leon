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
            distance += 1
            xor = xor & (xor - 1)
        return distance
