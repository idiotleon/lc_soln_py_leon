"""
    https://leetcode.com/problems/linked-list-frequency/

    Time Complexity:    O(L)
    Space Complexity:   O(L)

    Reference:
    https://leetcode.com/problems/linked-list-frequency/editorial/

    @author: Leon
"""

from ast import Dict
from typing import Optional

from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def frequencies_of_elements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_to_node: Dict[int, ListNode] = {}
        cur = head
        cur_freq = None
        while cur is not None:
            value = cur.val
            if value in num_to_node:
                num_to_node[value].val += 1
            else:
                new_node = ListNode(1, cur_freq)
                num_to_node[value] = new_node
                cur_freq = new_node
            cur = cur.next
        return cur_freq
