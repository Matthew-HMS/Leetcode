from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            
            current = current.next

        if list1 is None:
            current.next = list2
        if list2 is None:
            current.next = list1

        return dummy.next


s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

merged_head = s.mergeTwoLists(node1, node4)
current_node = merged_head
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = dummy = ListNode()
#         while list1 and list2:               
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#             cur.next = list1 if list1 else list2
            
#         return dummy.next