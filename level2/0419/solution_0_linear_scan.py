"""
    https://leetcode.com/problems/battleships-in-a-board/

    Time Complexity:    O(`LEN_R` * `LEN_C`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def count_battleships(self, board: List[List[str]]) -> int:
        LEN_R, LEN_C = len(board), len(board[0])
        count = 0
        for r in range(LEN_R):
            for c in range(LEN_C):
                if board[r][c] == '.':
                    continue
                if r > 0 and board[r - 1][c] == 'X':
                    continue
                if c > 0 and board[r][c - 1] == 'X':
                    continue
                count += 1
        return count
