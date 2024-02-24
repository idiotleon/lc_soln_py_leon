"""
    https://leetcode.com/problems/toeplitz-matrix/

    Time Complexity:    O(`LEN_R` * `LEN_C`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        LEN_R, LEN_C = len(matrix), len(matrix[0])
        for r in range(LEN_R - 1):
            for c in range(LEN_C - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True
