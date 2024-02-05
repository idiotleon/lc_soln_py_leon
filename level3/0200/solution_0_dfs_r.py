"""
    https://leetcode.com/problems/number-of-islands/

    Time Complexity:    O(`NR` * `NC`)
    Space Complexity:   O(`NR` * `NC`)

    Reference:
    https://leetcode.com/problems/number-of-islands/solutions/345981/python3-number-of-islands-bfs-dfs/
    https://leetcode.com/problems/number-of-islands/solutions/863366/python-3-dfs-bfs-union-find-all-3-methods-explanation/

    @author: Leon
"""

from ast import List


class Solution:
    DIRS = [0, -1, 0, 1, 0]

    def numIslands(self, grid: List[List[str]]) -> int:
        NR = len(grid)
        NC = len(grid[0])
        count = 0
        for r in range(NR):
            for c in range(NC):
                if grid[r][c] == '1':
                    self.dfs(r, c, grid)
                    count += 1
        return count

    def dfs(self, r, c, grid):
        NR = len(grid)
        NC = len(grid[0])
        grid[r][c] = '0'
        for d in range(4):
            r_next = r + self.DIRS[d]
            c_next = c + self.DIRS[d + 1]
            if 0 <= r_next < NR and 0 <= c_next < NC and grid[r_next][c_next] == '1':
                self.dfs(r_next, c_next, grid)
