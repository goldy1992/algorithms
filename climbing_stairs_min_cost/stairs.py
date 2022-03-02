from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if cost in (0, 1):
            return 0
        finish = len(cost)
        min_total_cost = [cost[0], cost[1]]

        for i in range(2, finish):
            min_total_cost.append(cost[i] + min(min_total_cost[i-1], min_total_cost[i-2]))

        return min(min_total_cost[finish-1], min_total_cost[finish-2])
