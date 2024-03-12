class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str1)
        b = len(str2)
        # find gcd(a,b)
        cd = []
        for i in range(1,min(a,b)+1):
            if a%i == 0 and b%i == 0:
                cd.append(i)
        
        if len(cd) == 0:
            return ""
        else:
            gcd = max(cd)

        output = ""
        for i in range(gcd):
            if str1[i] == str2[i]:
                output += str1[i]


        if len(output) == 0:
            return ""
        
        a_set = False
        b_set = False 
        for i in range(1, int(max(a,b)/len(output))+1):
            if output * i == str1:
                a_set = True
            if output * i == str2:
                b_set = True

        if a_set and b_set:
            return output
        else:
            return ""


    
s = Solution()
ans = s.gcdOfStrings("AB", "ABCABC")
print(ans)

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         # Check if concatenated strings are equal or not, if not return ""
#         if str1 + str2 != str2 + str1:
#             return ""
#         # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
#         from math import gcd
#         return str1[:gcd(len(str1), len(str2))]