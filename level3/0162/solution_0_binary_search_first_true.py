"""
    https://leetcode.com/problems/find-peak-element/

    Time Complexity:    O(lg(`LEN`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""

from ast import List


class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
