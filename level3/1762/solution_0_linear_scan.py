"""
    https://leetcode.com/problems/buildings-with-an-ocean-view/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def find_buildings(self, heights: List[int]) -> List[int]:
        LEN = len(heights)
        tallest = 0
        ans = []
        for idx in reversed(range(LEN)):
            if heights[idx] > tallest:
                tallest = heights[idx]
                ans.append(idx)
        ans.reverse()
        return ans
