from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        min_len = len(strs[0])

        for i in strs:
            if min_len > len(i):
                min_len = len(i)
            if len(i) == 0:
                return output
        for i in range(min_len):
            for j in range(len(strs)):
                if strs[0][i] != strs[j][i]:
                    return output
            output += strs[0][i]
        return output
    
s = Solution()
ans = s.longestCommonPrefix(["flower","flow","flight"])
print(ans)

# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans 