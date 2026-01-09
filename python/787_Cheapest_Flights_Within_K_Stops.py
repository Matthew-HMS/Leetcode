from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0

        for _ in range(k + 1):
            temp = dp[:]
            for flight in flights:
                if dp[flight[0]] != float('inf'):
                    temp[flight[1]] = min(temp[flight[1]], dp[flight[0]] + flight[2])
            dp = temp
        
        return dp[dst] if dp[dst] != float('inf') else -1

s = Solution()
ans = s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
print(ans)