"""
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        LEN = len(nums)
        if LEN < 2:
            return LEN
        lo = 0
        for hi in range(LEN):
            if hi > 0 and nums[hi - 1] == nums[hi]:
                continue
            nums[lo] = nums[hi]
            lo += 1
        return lo
