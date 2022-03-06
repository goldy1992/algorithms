from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        num_houses = len(nums)
        if num_houses == 1:
            return nums[0]

        if num_houses in (2, 3):
            return max(nums)

        # start at 0
        val1 = nums[0]
        val2 = max(nums[0], nums[1])

        for i in range(2, num_houses-1):
            tmp = val2
            val2 = max(val2, val1 + nums[i])
            val1 = tmp

        max_a = val2

        # start at 1
        val1 = nums[1]
        val2 = max(nums[1], nums[2])

        for i in range(3, num_houses):
            tmp = val2
            val2 = max(val2, val1 + nums[i])
            val1 = tmp

        max_b = val2

        return max(max_a, max_b)

