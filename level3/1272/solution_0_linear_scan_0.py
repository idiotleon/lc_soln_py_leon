"""
    https://leetcode.com/problems/remove-interval/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/remove-interval/editorial/?envType=weekly-question&envId=2024-02-15

    @author: Leon
"""


from ast import List


class Solution:
    def remove_interval(self, intervals: List[List[int]], to_be_removed: List[int]) -> List[List[int]]:
        # not used
        # LEN = len(intervals)
        remove_start, remove_end = to_be_removed
        ans = []

        for start, end in intervals:
            if start > remove_end or end < remove_start:
                ans.append([start, end])
            else:
                if start < remove_start:
                    ans.append([start, remove_start])
                if end > remove_end:
                    ans.append([remove_end, end])

        return ans
