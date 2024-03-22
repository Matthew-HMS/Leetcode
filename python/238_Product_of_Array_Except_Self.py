from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        current = 1
        for i in range(len(nums)): # left product
            ans[i] = current
            current *= nums[i]

        current = 1
        for i in range(len(nums)-1, -1, -1): # right product
            ans[i] *= current
            current *= nums[i]

        return ans

ans = Solution().productExceptSelf([-1,1,0,-3,3])
print(ans)

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
        
#         prefix = [1] * n
#         suffix = [1] * n
        
#         for i in range(1, n):
#             prefix[i] = prefix[i - 1] * nums[i - 1]
        
#         for i in range(n - 2, -1, -1):
#             suffix[i] = suffix[i + 1] * nums[i + 1]
        
#         answer = [prefix[i] * suffix[i] for i in range(n)]
        
#         return answer
