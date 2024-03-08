"""
    https://leetcode.com/problems/zigzag-iterator/

    Time Complexity:
        `init`:         O(`LEN`)
        `next`:         O(`LEN`)
        `has_next`:     O(1)
    Space Complexity:   O(`LEN`)

    Reference:
    https://leetcode.com/problems/zigzag-iterator/solutions/71786/python-o-1-space-solutions/

    @author: Leon
"""


from ast import List


class ZigzagIterator:
    def __init__(self, vectors: List[List[int]]):
        # not used
        # LEN = len(vectors)
        self.data = [(len(v), iter(v)) for v in vectors if v]

    def next(self) -> int:
        # the time complexity of this step: O(`LEN`)
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len - 1, iter))
        return next(iter)

    def has_next(self) -> bool:
        return bool(self.data)
