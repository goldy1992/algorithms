from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        num_houses = len(nums)
        if num_houses == 1:
            return nums[0]

        if num_houses == 2:
            return max(nums[0], nums[1])

        max_profit = [nums[0], max(nums[0], nums[1])]

        for i in range(2, num_houses):
            max_profit.append(max(max_profit[i-1], max_profit[i-2] + nums[i]))

        return max(max_profit[num_houses-1], max_profit[num_houses-2])

