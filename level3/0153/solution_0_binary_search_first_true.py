"""
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    Time Complexity:    O()
    Space Complexity:   O()

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""


from ast import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
