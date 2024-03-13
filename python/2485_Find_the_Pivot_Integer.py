class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            if (1+i)*i/2 == (i+n)*(n-i+1)/2:
                return i
        return -1
    

s = Solution()
ans = s.pivotInteger(1)
print(ans)