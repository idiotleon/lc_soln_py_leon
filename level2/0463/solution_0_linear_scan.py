"""
    https://leetcode.com/problems/island-perimeter/

    Time Complexity:    O(`LEN_R` * `LEN_C`)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        LEN_R, LEN_C = len(grid), len(grid[0])
        perimeter = 0
        for r in range(LEN_R):
            for c in range(LEN_C):
                if grid[r][c] != 1:
                    continue
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
        return perimeter
