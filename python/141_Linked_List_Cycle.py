# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
        return False


s = Solution()
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

ans = s.hasCycle(node1)
print(ans)