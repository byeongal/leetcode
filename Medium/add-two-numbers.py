from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_node_2_int(list_node: ListNode) -> int:
    ret = ""
    cur: ListNode = list_node
    while cur is not None:
        ret += f"{cur.val}"
        cur = cur.next
    return int(ret[::-1])


def int_2_list_node(int_val: int) -> ListNode:
    root: ListNode = ListNode(int_val % 10)
    cur = root
    while int_val:
        int_val //= 10
        if int_val != 0:
            cur.next = ListNode(int_val % 10)
            cur = cur.next
    return root


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        int_l1 = list_node_2_int(l1)
        int_l2 = list_node_2_int(l2)
        answer = int_l1 + int_l2
        return int_2_list_node(answer)
