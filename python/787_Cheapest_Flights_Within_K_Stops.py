from typing import List

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        start = []
        for i in range(len(flights)):
            if flights[i][0] == src:
                start.append(flights[i])


        prob = []
        for i in range(len(start)):
            spot = k
            total = 0
            end = False
            stop_p = start[i][1]
            start_p = start[i][0]
            # total += start[i][2]
            while spot >= 0:
                for i in range(len(flights)):
                    if start_p == flights[i][0] and stop_p == flights[i][1]:
                        total += flights[i][2]
                        spot -= 1
                        flights.remove(flights[i])
                        if stop_p == dst:
                            end = True
                            break
                        else:
                            start_p = stop_p
                            # start.append(flights[i])

                    elif start_p == flights[i][0]:
                        stop_p = flights[i][1]
                        total += flights[i][2]
                        spot -= 1
                        flights.remove(flights[i])
                        if stop_p == dst:
                            end = True
                            break
                        else:
                            start_p = stop_p
                            # start.append(flights[i])

                # for i in range(len(flights)):
                #     if stop_p == flights[i][0]:
                #         start_p = stop_p
                #         stop_p = flights[i][1]
            if end == True:
                prob.append(total)

        print(start)
        print(prob)

s = Solution()
ans = s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
print(ans)