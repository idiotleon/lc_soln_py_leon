"""
    https://leetcode.com/problems/flatten-2d-vector/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(`LEN`)

    @author: Leon
"""


from ast import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.idx = 0
        self.nums: List[int] = []
        for ele in vec:
            for num in ele:
                self.nums.append(num)
        self.LEN = len(self.nums)

    def next(self) -> int:
        ans = self.nums[self.idx]
        self.idx += 1
        return ans

    def hasNext(self) -> bool:
        return self.idx < self.LEN
