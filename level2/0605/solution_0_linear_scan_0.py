"""
    https://leetcode.com/problems/can-place-flowers/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/can-place-flowers/editorial/comments/781356

    @author: Leon
"""


from ast import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        LEN = len(flowerbed)
        FLOWER, EMPTY = 1, 0
        capacity = 0
        padded = [0] + flowerbed + [0]
        for idx in range(1, LEN + 1):
            if padded[idx] == padded[idx - 1] == padded[idx + 1] == 0:
                capacity += 1
                if capacity >= n:
                    return True
                padded[idx] = FLOWER
        return n == 0
