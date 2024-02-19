"""
    https://leetcode.com/problems/remove-interval/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/remove-interval/editorial/comments/764110
    https://leetcode.com/problems/remove-interval/editorial/?envType=weekly-question&envId=2024-02-15

    @author: Leon
"""


from ast import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], to_be_removed: List[int]) -> List[List[int]]:
        # not used
        # LEN = len(intervals)
        ans = []
        start_remove, end_remove = to_be_removed

        for start, end in intervals:
            if (idx := min(end, start_remove)) > start:
                ans.append([start, idx])
            if (idx := max(start, end_remove)) < end:
                ans.append([idx, end])

        return ans
