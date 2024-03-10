"""
    https://leetcode.com/problems/linked-list-frequency/

    Time Complexity:    O(L)
    Space Complexity:   O(L)

    @author: Leon
"""

from collections import defaultdict
from typing import Optional

from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def frequencies_of_elements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_to_freq = defaultdict(int)
        cur = head
        while cur is not None:
            value = cur.val
            num_to_freq[value] += 1
            cur = cur.next
        dummy = ListNode(-1)
        cur = dummy
        for freq in num_to_freq.values():
            new_node = ListNode(freq)
            cur.next = new_node
            cur = cur.next
        return dummy.next
