"""
    https://leetcode.com/problems/nested-list-weight-sum/

    Time Complexity:    O(N)
    Space Complexity:   O(N)

    @author: Leon
"""


from ast import List

from util.other.NestedInteger import NestedInteger


class Solution:
    def depthSum(self, nested_list: List[NestedInteger]) -> int:
        return self.dfs(nested_list, 1)

    def dfs(self, nested_list: List[NestedInteger], depth: int) -> int:
        sum = 0
        for num in nested_list:
            if num.is_integer():
                sum += num.get_integer() * depth
            else:
                sum += self.dfs(num.get_list(), depth + 1)
        return sum
