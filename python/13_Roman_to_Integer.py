class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            if s[i] == 'I':
                total += 1
            elif s[i] == 'V':
                total += 5
            elif s[i] == 'X':
                total += 10
            elif s[i] == 'L':
                total += 50
            elif s[i] == 'C':
                total += 100
            elif s[i] == 'D':
                total += 500
            elif s[i] == 'M':
                total += 1000
        for i in range(len(s)-1):
            if s[i] == 'I' and s[i+1] == 'V':
                total -= 2
            if s[i] == 'I' and s[i+1] == 'X':
                total -= 2
            if s[i] == 'X' and s[i+1] == 'L':
                total -= 20
            if s[i] == 'X' and s[i+1] == 'C':
                total -= 20
            if s[i] == 'C' and s[i+1] == 'D':
                total -= 200
            if s[i] == 'C' and s[i+1] == 'M':
                total -= 200
        return total
    

s = Solution()
ans = s.romanToInt("MCMXCIV")
print(ans)


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         m = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         ans = 0
        
#         for i in range(len(s)):
#             if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
#                 ans -= m[s[i]]
#             else:
#                 ans += m[s[i]]
        
#         return ans