"""
    https://leetcode.com/problems/sort-array-by-parity/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        while lo < hi:
            while lo < hi and nums[lo] % 2 == 0:
                lo += 1
            while lo < hi and nums[hi] % 2 == 1:
                hi -= 1
            nums[lo], nums[hi] = nums[hi], nums[lo]
        return nums
