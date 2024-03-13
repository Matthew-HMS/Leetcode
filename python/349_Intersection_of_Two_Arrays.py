from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] in ans:
                    pass
                else:
                    ans.append(nums1[i])
                i += 1
                j = 0

            elif j == len(nums2)-1:
                i += 1
                j = 0

            else:
                j += 1

        return ans


s = Solution()
ans = s.intersection([4,9,9], [9,4,9,8,4])
print(ans)


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         set1 = set(nums1)   # set() remove any duplicate elements from the input lists
#         set2 = set(nums2)
#         return list(set1.intersection(set2))