"""
    https://leetcode.com/problems/remove-linked-list-elements/

    Time Complexity:    O(L)
    Space Complexity:   O(1)

    @author: Leon
"""


from typing import Optional
from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def remove_elements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        prev.next = head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
