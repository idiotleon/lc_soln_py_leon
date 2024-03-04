"""
    https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

    Time Complexity:    O()
    Space Complexity:   O(`LEN1` + `LEN2`) ~ O(max(`LEN1`, `LEN2`))

    Reference:
    https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solutions/1823242/clean-solutions-for-meta-interview-with-potential-follow-ups/

    @author: Leon
"""


from ast import Dict, List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_to_val = [(idx, num)
                           for idx, num in enumerate(nums) if num != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        nums1 = self.idx_to_val
        nums2 = vec.idx_to_val
        return self.multiply(nums1, nums2)

    def multiply(self, nums1: Dict[int, int], nums2: Dict[int, int]) -> int:
        LEN1, LEN2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        sum = 0
        while idx1 < LEN1 and idx2 < LEN2:
            if nums1[idx1][0] == nums2[idx2][0]:
                sum += nums1[idx1][1] * nums2[idx2][1]
                idx1 += 1
                idx2 += 1
            elif nums1[idx1][0] < nums2[idx2][0]:
                idx1 += 1
            else:
                idx2 += 1
        return sum
