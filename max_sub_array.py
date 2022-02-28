class Solution:

    def maxSubArray(self, nums):

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        current_max = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            if n >= 0:
                if current_sum < 0:
                    current_sum = n
                else:
                    current_sum += n
            else:
                if current_sum + n > 0:
                    current_sum += n
                else:
                    current_sum = n

            if current_sum > current_max:
                current_max = current_sum

        return current_max