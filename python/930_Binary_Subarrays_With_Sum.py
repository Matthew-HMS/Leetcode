from typing import List

# This will get TLE
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = 0
        total = 0
        for i in nums:
            total += i
        if total < goal:
            return 0
        for i in range(goal, len(nums)+1): # 2,2,2..,3,3,3
            for j in range(len(nums)-i+1): # start form 0
                total = sum(nums[j:j+i])
                if total == goal and len(nums[j:j+i]) != 0:
                    # print(nums[j:j+i])
                    counter += 1

        return counter
    

ans = Solution().numSubarraysWithSum([0, 1, 1, 0, 0, 1, 0, 1, 1], 5)
print(ans)

# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         count = {0: 1}
#         curr_sum = 0
#         total_subarrays = 0
        
#         for num in nums:
#             curr_sum += num
#             if curr_sum - goal in count:
#                 total_subarrays += count[curr_sum - goal]
#             count[curr_sum] = count.get(curr_sum, 0) + 1

#         return total_subarrays