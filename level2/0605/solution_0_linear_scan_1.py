"""
    https://leetcode.com/problems/can-place-flowers/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        LEN = len(flowerbed)
        FLOWER, EMPTY = 1, 0
        capacity = 0
        for idx in range(LEN):
            if flowerbed[idx] == EMPTY \
                    and (idx == 0 or flowerbed[idx - 1] == EMPTY) \
                    and (idx == LEN - 1 or flowerbed[idx + 1] == EMPTY):
                capacity += 1
                if capacity >= n:
                    return True
                flowerbed[idx] = FLOWER
        return n == 0
