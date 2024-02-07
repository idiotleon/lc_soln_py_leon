"""
    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""


from ast import List


class BinarySearch:
    def binary_search_last_true(nums: List[int], target: int):
        # to assume: the array to search
        # nums = [1, 2, 3, 4, 5, 7, 8, 6]
        #         T, T, T, T, T, F, F, F
        #                     *
        LEN = len(nums)
        lo, hi = 0, LEN - 1
        while lo < hi:
            # right biased `mid`
            mid = lo + (hi - lo + 1) // 2
            # to assume: the target is 6
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
        return lo
