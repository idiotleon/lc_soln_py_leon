"""
    https://leetcode.com/problems/squares-of-a-sorted-array/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(`LEN`) / O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        idx = LEN - 1
        ans = [0] * LEN
        while idx >= 0:
            if abs(nums[lo]) < abs(nums[hi]):
                ans[idx] = nums[hi] * nums[hi]
                hi -= 1
            else:
                ans[idx] = nums[lo] * nums[lo]
                lo += 1
            idx -= 1
        return ans
