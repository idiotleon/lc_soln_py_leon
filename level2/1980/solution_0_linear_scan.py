"""
    https://leetcode.com/problems/find-unique-binary-string/

    Time Complexity:    O(`n` ^ 2)
    Space Complexity:   O(1)

    @author: Leon
"""


from ast import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set()
        for num in nums:
            seen.add(int(num, 2))

        LEN = len(nums)
        for num in range(LEN + 1):
            if num not in seen:
                ans = bin(num)[2:]
                return "0" * (LEN - len(ans)) + ans

        return ""
