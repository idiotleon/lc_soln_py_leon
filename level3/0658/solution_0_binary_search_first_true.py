"""
    https://leetcode.com/problems/find-k-closest-elements/

    Time Complexity:    O(lg(`LEN`))
    Space Complexity:   O(1)

    @author: Leon
"""

from ast import List


class Solution:
    def find_closest_elements(self, nums: List[int], k: int, x: int) -> List[int]:
        LEN = len(nums)
        lo, hi = 0, LEN - k
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if x - nums[mid] <= nums[mid + k] - x:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo:lo + k]
