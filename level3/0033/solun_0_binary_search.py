"""
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    Time Complexity:    O(lg(`LEN`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""

from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
