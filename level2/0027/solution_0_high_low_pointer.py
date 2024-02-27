"""
    https://leetcode.com/problems/remove-element/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        LEN = len(nums)
        lo = 0
        for hi in range(LEN):
            if nums[hi] == val:
                continue
            nums[lo] = nums[hi]
            lo += 1
        return lo
