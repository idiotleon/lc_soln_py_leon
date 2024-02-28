"""
    https://leetcode.com/problems/longest-continuous-increasing-subsequence/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def find_length_of_LCIS(self, nums: List[int]) -> int:
        LEN = len(nums)
        idx = 1
        running, longest = 1, 1
        while idx < LEN:
            if nums[idx - 1] < nums[idx]:
                running += 1
                longest = max(longest, running)
            else:
                running = 1
            idx += 1
        return longest
