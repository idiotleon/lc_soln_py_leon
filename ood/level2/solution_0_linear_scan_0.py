"""
    https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

    Time Complexity:    O()
    Space Complexity:   O()

    Reference:
    https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solutions/1823242/clean-solutions-for-meta-interview-with-potential-follow-ups/

    @author: Leon
"""


from ast import Dict, List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_to_val: Dict[int, int] = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.idx_to_val[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum = 0
        for (idx, num) in vec.idx_to_val.items():
            if idx in self.idx_to_val:
                sum += num * self.idx_to_val[idx]
        return sum
