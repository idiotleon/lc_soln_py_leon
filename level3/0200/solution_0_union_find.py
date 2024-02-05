"""
    https://leetcode.com/problems/number-of-islands/

    Time Complexity:    O(`NR` * `NC`)
    Space Complexity:   O(`NR` * `NC`)

    Reference:
    https://leetcode.com/problems/number-of-islands/solutions/863366/python-3-dfs-bfs-union-find-all-3-methods-explanation/

    @author: Leon
"""


from ast import List


class UF:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.n = n
        self.size = n

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.size -= 1
            self.roots[root_x] = root_y

    def find(self, x):
        if x != self.roots[x]:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        NR, NC = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for r in range(NR):
            for c in range(NC):
                if grid[r][c] == "1":
                    d[r, c] = idx
                    idx += 1
        uf = UF(idx)
        for r in range(NR):
            for c in range(NC):
                if grid[r][c] == "1":
                    if r > 0 and grid[r - 1][c] == "1":
                        uf.union(d[r - 1, c], d[r, c])
                    if c > 0 and grid[r][c - 1] == "1":
                        uf.union(d[r, c - 1], d[r, c])
        return uf.size
