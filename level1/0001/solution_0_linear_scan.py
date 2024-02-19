"""
    https://leetcode.com/problems/two-sum/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(`LEN`)

    Reference:
    https://leetcode.com/problems/two-sum/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # not used
        # LEN = len(nums)
        num_to_idx = {}
        for idx, num in enumerate(nums):
            num_to_idx[num] = idx
        for idx, num in enumerate(nums):
            expected = target - num
            if expected in num_to_idx and num_to_idx[expected] != idx:
                return [idx, num_to_idx[expected]]
        # unreachable
        return []
