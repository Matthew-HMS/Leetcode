class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if len(word1) < len(word2):
            short = word1
            long = word2
        else:
            short = word2
            long = word1

        output = ""
        for i in range(len(short)):
            output = output + word1[i] + word2[i]
        
        output += long[len(short):]

        return output
    
s = Solution()
ans = s.mergeAlternately("abc", "pqrst")
print(ans)

# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         result = []
#         i = 0
#         while i < len(word1) or i < len(word2):
#             if i < len(word1):
#                 result.append(word1[i])
#             if i < len(word2):
#                 result.append(word2[i])
#             i += 1
#         return ''.join(result)