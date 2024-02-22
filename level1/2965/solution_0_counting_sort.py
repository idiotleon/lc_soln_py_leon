"""
    https://leetcode.com/problems/find-common-elements-between-two-arrays/

    Time Complexity:    O(`RANGE`) ~ O(1)
    Space Complexity:   O(`RANGE`) ~ O(1)

    @author: Leon
"""

from ast import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        RANGE = 100 + 1
        FREQS1, FREQS2 = [0] * RANGE, [0] * RANGE
        for num in nums1:
            FREQS1[num] += 1
        for num in nums2:
            FREQS2[num] += 1
        count1, count2 = 0, 0
        for num in nums1:
            if FREQS2[num] > 0:
                count1 += 1
        for num in nums2:
            if FREQS1[num] > 0:
                count2 += 1
        return [count1, count2]
