"""
    https://leetcode.com/problems/generate-parentheses/

    Time Complexity:    O(4 ^ n / (n ^ (1 / 2)))
    Space Complexity:   O(`n`)

    Reference:
    https://leetcode.com/problems/generate-parentheses/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        ans: List[str] = []
        self.backtrack([], 0, 0, n, ans)
        return ans

    def backtrack(self, cur: List[str], count_open: int, count_closed: int, n: int, ans: List[str]):
        if len(cur) == 2 * n:
            ans.append("".join(cur))
            return

        if count_open < n:
            cur.append("(")
            self.backtrack(cur, count_open + 1, count_closed, n, ans)
            cur.pop()

        if count_closed < count_open:
            cur.append(")")
            self.backtrack(cur, count_open, count_closed + 1, n, ans)
            cur.pop()
