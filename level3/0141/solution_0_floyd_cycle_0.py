"""
    https://leetcode.com/problems/linked-list-cycle/

    Time Complexity:    O(L)
    Space Complexity:   O(1)

    @author: Leon
"""


from typing import Optional

from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
