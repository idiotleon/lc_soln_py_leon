"""
    https://leetcode.com/problems/add-two-numbers/

    Time Complexity:    O(max(m, n))
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/add-two-numbers/editorial/

    @author: Leon
"""

from typing import Optional

from util.linkedlist.linkedlist_node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        cur = dummy_head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            sum = val_l1 + val_l2 + carry
            carry = sum // 10
            new_node = ListNode(sum % 10)
            cur.next = new_node
            cur = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
