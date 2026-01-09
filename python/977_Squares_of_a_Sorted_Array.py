from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = []
        for i in range(len(nums)):
            square.append(nums[i]*nums[i])
        
        return sorted(square)
    

s = Solution()
ans = s.sortedSquares([-4,-1,0,3,10])
print(ans)
        

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         squares = [num * num for num in nums]
#         squares.sort()
#         return squares