"""
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    Time Complexity:    O(L)
    Space Complexity:   O(1)

    @author: Leon
"""


from typing import Optional

from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        lo, hi = dummy, dummy
        for _ in range(n + 1):
            hi = hi.next
        while hi:
            lo = lo.next
            hi = hi.next
        lo.next = lo.next.next

        return dummy.next
