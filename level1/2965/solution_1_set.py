"""
    https://leetcode.com/problems/find-common-elements-between-two-arrays/

    Time Complexity:    O(`LEN1` + `LEN2`) ~ O(max(`LEN1`, `LEN2`))
    Space Complexity:   O(`LEN1` + `LEN2`) ~ O(max(`LEN1`, `LEN2`))

    Reference:
    https://leetcode.com/problems/find-common-elements-between-two-arrays/solutions/4382829/c-java-python-javascript-easy-approach-explained/

    @author: Leon
"""


from ast import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # not used
        # LEN1, LEN2 = len(nums1), len(nums2)
        SET1, SET2 = set(nums1), set(nums2)

        count1 = sum(1 for num in nums1 if num in SET2)
        count2 = sum(1 for num in nums2 if num in SET1)

        return [count1, count2]
