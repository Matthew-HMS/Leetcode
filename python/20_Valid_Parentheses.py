class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        wait = []
        for i in s:
            stack.append(i)
        n = len(stack)
        if n % 2 != 0:
            return False
        
        while len(stack) != 0:
            if len(stack) != 0:
                wait.append(stack[-1])
                stack.pop()
            if len(wait) > 1:
                if wait[-1] == '(' and wait[-2] == ')':
                    wait.pop()
                    wait.pop()
                elif wait[-1] == '[' and wait[-2] == ']':
                    wait.pop()
                    wait.pop()
                elif wait[-1] == '{' and wait[-2] == '}':
                    wait.pop()
                    wait.pop()
        if len(wait) > 1:
                if wait[-1] == '(' and wait[-2] == ')':
                    wait.pop()
                    wait.pop()
                elif wait[-1] == '[' and wait[-2] == ']':
                    wait.pop()
                    wait.pop()
                elif wait[-1] == '{' and wait[-2] == '}':
                    wait.pop()
                    wait.pop()

        if len(wait) == 0:
            return True
        else:
            return False


s = Solution()
ans = s.isValid("(){}}{")
print(ans)


# class Solution(object):
#     def isValid(self, s):
#         stack = [] # create an empty stack to store opening brackets
#         for c in s: # loop through each character in the string
#             if c in '([{': # if the character is an opening bracket
#                 stack.append(c) # push it onto the stack
#             else: # if the character is a closing bracket
#                 if not stack or \
#                     (c == ')' and stack[-1] != '(') or \
#                     (c == '}' and stack[-1] != '{') or \
#                     (c == ']' and stack[-1] != '['):
#                     return False # the string is not valid, so return false
#                 stack.pop() # otherwise, pop the opening bracket from the stack
#         return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
#                          # so the string is valid, otherwise, there are unmatched opening brackets, so return false