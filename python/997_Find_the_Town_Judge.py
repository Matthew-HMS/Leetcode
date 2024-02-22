from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_dict = {}
        truster_dict = {}
        for i in range(len(trust)):
            truster, trusted = trust[i]
            if trusted not in trusted_dict:
                trusted_dict[trusted] = 1
            else:
                trusted_dict[trusted] += 1

            if truster not in truster_dict:
                truster_dict[truster] = 1
            else:
                truster_dict[truster] += 1

        judge = 0
        for key, value in trusted_dict.items():
            if value == n - 1:
                judge = key

        if n == 1:
            return 1
        elif judge == 0 or judge in truster_dict:
            return -1
        else:
            return judge

s = Solution()
ans = s.findJudge(2, [[1,2]])
print(ans)


# class Solution:
#     def findJudge(self, N: int, trust: List[List[int]]) -> int:
#         in_degree = [0] * (N + 1)
#         out_degree = [0] * (N + 1)
#         for a in trust:
#             out_degree[a[0]] += 1
#             in_degree[a[1]] += 1
#         for i in range(1, N + 1):
#             if in_degree[i] == N - 1 and out_degree[i] == 0:
#                 return i
#         return -1
