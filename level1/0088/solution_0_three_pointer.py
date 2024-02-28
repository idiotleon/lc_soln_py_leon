"""
    https://leetcode.com/problems/merge-sorted-array/

    Time Complexity:    O(`m` + `n`) ~ O(max(`m`, `n`)) ~ O(`m`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        RANGE = int(1e9) + 7
        idx = m + n - 1
        idx1, idx2 = m - 1, n - 1
        while idx >= 0:
            num1 = nums1[idx1] if idx1 >= 0 else -RANGE
            num2 = nums2[idx2] if idx2 >= 0 else -RANGE
            if num1 > num2:
                nums1[idx] = num1
                idx1 -= 1
            else:
                nums1[idx] = num2
                idx2 -= 1
            idx -= 1
