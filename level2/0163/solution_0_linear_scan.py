"""
    https://leetcode.com/problems/missing-ranges/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/missing-ranges/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def find_missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        LEN = len(nums)
        if LEN == 0:
            return [[lower, upper]]

        ans: List[[int]] = []
        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])

        for idx in range(LEN - 1):
            if nums[idx + 1] - nums[idx] <= 1:
                continue
            ans.append([nums[idx] + 1, nums[idx + 1] - 1])

        if upper > nums[-1]:
            ans.append([nums[-1] + 1, upper])

        return ans
