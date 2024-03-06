"""
    https://leetcode.com/problems/linked-list-cycle/

    Time Complexity:    O(L)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/linked-list-cycle/editorial/

    @author: Leon
"""


from typing import Optional

from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head.next
        slow = head

        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return True
