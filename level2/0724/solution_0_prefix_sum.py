"""
    https://leetcode.com/problems/find-pivot-index/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # not used
        # LEN = len(nums)
        SUM = sum(nums)
        lo_sum, hi_sum = 0, SUM
        for (idx, num) in enumerate(nums):
            hi_sum -= num
            if lo_sum == hi_sum:
                return idx
            lo_sum += num
        # unreachable
        return -1
