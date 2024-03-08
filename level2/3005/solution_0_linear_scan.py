"""
    https://leetcode.com/problems/count-elements-with-maximum-frequency/

    Time Complexity:    O(`RANGE`)
    Space Complexity:   O(`RANGE`) ~ O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        RANGE = 100 + 1
        freqs = [0] * RANGE
        for num in nums:
            freqs[num] += 1

        most = 1
        count = 0
        for freq in freqs:
            if freq > most:
                most = freq
                count = freq
            elif freq == most:
                count += freq

        return count
