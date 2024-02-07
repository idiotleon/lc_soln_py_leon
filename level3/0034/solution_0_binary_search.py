"""
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

    Time Complexity:    O(lg(`LEN`))
    Space Compleixty:   O(1)

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""


from ast import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # sanity check required
        if not nums:
            return [-1, -1]
        first = self.first_true(nums, target)
        last = self.last_true(nums, target)
        # sanity check, especially the 2nd segment, required
        if first > last or nums[first] != target:
            return [-1, -1]
        return [first, last]

    def first_true(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def last_true(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
        return lo
