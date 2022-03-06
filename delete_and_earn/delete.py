from typing import List


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        calculation = [n for n in range(0, max(nums)+1)]
        arr_size = len(calculation)
        for i in range(0,arr_size):
            calculation[i] = 0

        for n in nums:
            calculation[n] += n

        arr_size = len(calculation)
        for idx in range(2, arr_size):
            calculation[idx] = max(calculation[idx] + calculation[idx-2], calculation[idx-1])

        return calculation[arr_size-1]

