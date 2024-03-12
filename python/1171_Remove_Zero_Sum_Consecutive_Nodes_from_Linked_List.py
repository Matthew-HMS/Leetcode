from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        total = 0
        arr = []
        while head != None:
            total += head.val
            if head.val == 0:
                pass
            else:
                arr.append(head.val)
            head = head.next

        count = 0
        while count < len(arr):
            target = arr[count]
            add_sum = arr[count]


            for j in range(count+1, len(arr)):
                add_sum += arr[j]
                if add_sum == 0:
                    arr = arr[j+1:]
                    count = -1
                    break
                elif add_sum == target:
                    arr = arr[:count+1] + arr[j+1:]
                    count = -1
                    break

            count += 1


        dummy = ListNode(0)
        ptr = dummy
        for i in arr:
            ptr.next = ListNode(i)
            ptr = ptr.next


        return dummy.next


def print_list(node):
    while node is not None:
        print(node.val, end=' ')
        node = node.next


s = Solution()
node1 = ListNode(2)
node2 = ListNode(2)
node3 = ListNode(-2)
node4 = ListNode(1)
node5 = ListNode(-1)
node6 = ListNode(-1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


ans = s.removeZeroSumSublists(node1)
print_list(ans)

# class Solution:
#     def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         prefix_sum = 0
#         prefix_sums = {0: dummy}
#         current = head

#         while current:
#             prefix_sum += current.val
#             if prefix_sum in prefix_sums:
#                 to_delete = prefix_sums[prefix_sum].next
#                 temp_sum = prefix_sum + to_delete.val
#                 while to_delete != current:
#                     del prefix_sums[temp_sum]
#                     to_delete = to_delete.next
#                     temp_sum += to_delete.val
#                 prefix_sums[prefix_sum].next = current.next
#             else:
#                 prefix_sums[prefix_sum] = current
#             current = current.next

#         return dummy.next