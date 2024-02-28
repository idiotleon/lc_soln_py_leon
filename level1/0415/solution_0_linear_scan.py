"""
    https://leetcode.com/problems/add-strings/

    Time Complexity:    O(`LEN1` + `LEN2`) ~ O(max(`LEN1`, `LEN2`))
    Space Complexity:   O(max(`LEN1`, `LEN2`) / O(1)

    Reference:
    https://leetcode.com/problems/add-strings/editorial/

    @author: Leon
"""


class Solution:
    def add_strings(self, num1: str, num2: str) -> str:
        LEN1, LEN2 = len(num1), len(num2)
        res = []
        carry = 0
        idx1, idx2 = LEN1 - 1, LEN2 - 1
        while idx1 >= 0 or idx2 >= 0 or carry > 0:
            digit1 = ord(num1[idx1]) - ord('0') if idx1 >= 0 else 0
            digit2 = ord(num2[idx2]) - ord('0') if idx2 >= 0 else 0
            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10
            res.append(digit)
            idx1 -= 1
            idx2 -= 1
        return ''.join(str(s) for s in res[::-1])
