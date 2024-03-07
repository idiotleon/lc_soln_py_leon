"""
    https://leetcode.com/problems/middle-of-the-linked-list/

    Time Complexity:    O(L)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/middle-of-the-linked-list/editorial/

    @author: Leon
"""


from typing import Optional

from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
