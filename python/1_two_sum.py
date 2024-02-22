from typing import List

# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j]

                
s = Solution()
ans = s.twoSum([2,3,6,14,56], 9)
print(ans)

#O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_dict = {}
#         for i, num in enumerate(nums):
#             if target - num in num_dict:
#                 return [num_dict[target - num], i]
#             num_dict[num] = i