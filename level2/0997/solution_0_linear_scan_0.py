"""
    https://leetcode.com/problems/find-the-town-judge/

    Time Complexity:    O(`n`)
    Space Complexity:   O(`RANGE`) ~ O(1)

    Reference:
    https://leetcode.com/problems/find-the-town-judge/editorial/?envType=daily-question&envId=2024-02-22

    @author: Leon
"""


from ast import List


class Solution:
    def findJudge(self, n: int, trusts: List[List[int]]) -> int:
        if n == 1:
            return 1
        RANGE = n + 1
        degrees = [0] * RANGE
        for (outdegree, indegree) in trusts:
            degrees[outdegree] -= 1
            degrees[indegree] += 1
        for (idx, degree) in enumerate(degrees):
            if degree == n - 1:
                return idx
        return -1
