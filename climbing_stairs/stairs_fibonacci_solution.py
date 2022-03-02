class Solution:
    def climbStairs(self, n: int) -> int:
        values = [0, 1, 2]

        for i in range(3, n+1):
            values.append(values[i-1] + values[i-2])

        return values[n]