"""
    https://leetcode.com/problems/zigzag-iterator/

    Time Complexity:
        `init`:         O(`LEN`)
        `next`:         O(1)
        `has_next`:     O(1)
    Space Complexity:   O(`LEN`)

    Reference:
    https://leetcode.com/problems/zigzag-iterator/solutions/71786/python-o-1-space-solutions/

    @author: Leon
"""


from ast import List
import collections


class ZigzagIterator:
    def __init__(self, vectors: List[List[int]]):
        # not used
        # LEN = len(vectors)
        deques = collections.deque()
        for v in vectors:
            if bool(v):
                deques.append((len(v), iter(v)))
        self.data = deques

    def next(self) -> int:
        len, iter = self.data.popleft()
        if len > 1:
            self.data.append((len - 1, iter))
        return next(iter)

    def has_next(self) -> bool:
        return bool(self.data)
