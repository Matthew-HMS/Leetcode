from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        if nums1[0] > nums2[-1] or nums2[0] > nums1[-1]:
            return -1

        if nums1[0] < nums2[0]:
            start = nums2
            compare = nums1
        elif nums1[0] == nums2[0]:
            return nums1[0]
        else:
            start = nums1
            compare = nums2

        for i in start:
            for j in compare:
                if i < j:
                    break
                elif i == j:
                    return i
    
        return -1



s = Solution()
list1 = [4,6]
list2 = [2,3,5,7,9,10]
ans = s.getCommon(list1, list2)
print(ans)

# class Solution:
#     def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
#         i = 0
#         j = 0
#         common = float('inf')

#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 common = nums1[i]
#                 break
#             elif nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 j += 1
        
#         return common if common != float('inf') else -1