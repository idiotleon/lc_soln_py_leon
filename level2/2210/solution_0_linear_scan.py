"""
    https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/count-hills-and-valleys-in-an-array/solutions/1866666/count-hills-and-valleys-java-space-o-1-time-o-n-simple-solution/

    @author: Leon
"""


from ast import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        LEN = len(nums)
        last = nums[0]
        count = 0
        for idx in range(1, LEN - 1):
            if (last < nums[idx] and nums[idx] > nums[1 + idx]) or (last > nums[idx] and nums[idx] < nums[1 + idx]):
                count += 1
            if nums[idx] != nums[1 + idx]:
                last = nums[idx]
        return count
