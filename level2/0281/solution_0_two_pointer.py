"""
    https://leetcode.com/problems/zigzag-iterator/

    Time Complexity:
        `init`:         O(`LEN1` + `LEN2`) ~ O(max(`LEN1`, `LEN2`))
        `next`:         O(1)
        `has_next`:     O(1)
    Space Complexity:   O(`LEN1` + `LEN2`) ~ O(max(`LEN1`, `LEN2`))

    @author: Leon
"""


from ast import List
import collections


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        # not used
        # LEN1, LEN2 = len(v1), len(v2)
        deque1, deque2 = collections.deque(), collections.deque()
        for num1 in v1:
            deque1.append(num1)
        for num2 in v2:
            deque2.append(num2)
        self.deques = collections.deque()
        if deque1:
            self.deques.append(deque1)
        if deque2:
            self.deques.append(deque2)

    def next(self) -> int:
        deque = self.deques.popleft()
        ans = deque.popleft()
        if deque:
            self.deques.append(deque)
        return ans

    def has_next(self) -> bool:
        return self.deque
