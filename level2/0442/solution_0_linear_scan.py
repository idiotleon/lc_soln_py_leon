"""
    https://leetcode.com/problems/find-all-duplicates-in-an-array/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/find-all-duplicates-in-an-array/editorial/

    @author: Leon
"""

from ast import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # not used
        # LEN = len(nums)

        ans = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] > 0:
                nums[idx] *= -1
            else:
                ans.append(idx + 1)

        return ans
