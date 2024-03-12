class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # find intersection from order
        # add s remains
        output = ""
        for i in order:
            for j in range(len(s)):
                if i == s[j]:
                    output += i
                    s = s[:j] + s[j+1:]
                    break
        
        for i in s:
            if i not in output:
                output += i
            else:
                for j in range(len(output)):
                    if i == output[j]:
                        output = output[:j] + i + output[j:]
                        break
            

        return output

s = Solution()
ans = s.customSortString("bcafg", "abcd")
print(ans)


# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         char_count = {char: 0 for char in order}
#         for char in s:
#             if char in char_count:
#                 char_count[char] += 1
    
#         sorted_s = ''
#         for char in order:
#             sorted_s += char * char_count[char]
    
#         for char in s:
#             if char not in order:
#                 sorted_s += char

#         return sorted_s