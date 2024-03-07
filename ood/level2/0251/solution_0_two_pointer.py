"""
    https://leetcode.com/problems/flatten-2d-vector/

    Time Complexity:    O(N * average_length_vector)
    Space Complexity:   O(average_length_vector)

    @author: Leon
"""


from ast import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.outer = 0
        self.inner = 0
        self.vec = vec
        self.LEN = len(vec)

    def next(self) -> int:
        self.move()
        ans = self.vec[self.outer][self.inner]
        self.inner += 1
        return ans

    def hasNext(self) -> bool:
        self.move()
        return self.outer < self.LEN

    def move(self):
        while self.outer < self.LEN and self.inner == len(self.vec[self.outer]):
            self.outer += 1
            self.inner = 0
