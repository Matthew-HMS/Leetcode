from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        temp = []
        while current is not None:
            temp.append(current.val)
            current = current.next

        n = len(temp)//2
        if len(temp) % 2 == 0:
            for i in range(n):
                if temp[n-1-i] != temp[n+i]:
                    return False
            return True
        else:
            for i in range(n):
                if temp[n-1-i] != temp[n+1+i]:
                    return False
            return True
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(1)
node1.next = node2
node2.next = node3

ans = Solution().isPalindrome(node1)
print(ans)

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         list_vals = []
#         while head:
#             list_vals.append(head.val)
#             head = head.next
        
#         left, right = 0, len(list_vals) - 1
#         while left < right and list_vals[left] == list_vals[right]:
#             left += 1
#             right -= 1
#         return left >= right

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         list_vals = []
#         stack = []
#         curr = head
#         while curr:
#             stack.append(curr.val)
#             curr = curr.next
#         curr = head
#         while curr and curr.val == stack.pop():
#             curr = curr.next
#         return curr is None