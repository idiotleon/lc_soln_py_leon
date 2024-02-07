"""
    Time Complexity:    O(lg(`LEN`))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/

    @author: Leon
"""


from ast import List


class BinarySearch:
    def binary_search_first_true(nums: List[int], target: int) -> int:
        # to assume: the arrays to search
        # nums1 = [1, 2, 3, 4, 5, 7, 8, 6]
        #          T, T, T, T, T, F, F, F
        #          *
        # nums2 = [1, 2, 3, 4, 5, 7, 8, 6]
        #          F, F, F, F, F, T, T, T
        #                         *
        LEN = len(nums)
        lo, hi = 0, LEN
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                hi = mid
            else:
                lo = mid + 1
        return lo
