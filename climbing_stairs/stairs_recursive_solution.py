class Solution:
    count = 0

    def climbStairs(self, n: int) -> int:
        current_pos = 0
        self.climb(current_pos, n)
        return self.count


    def climb(self, current_pos, target: int):
        if (current_pos + 2) <= target:
            new_pos = current_pos + 2
            self.climb(new_pos, target)

        if (current_pos + 1) <= target:
            new_pos = current_pos + 1
            self.climb(new_pos, target)

        if current_pos >= target:
            self.count += 1




