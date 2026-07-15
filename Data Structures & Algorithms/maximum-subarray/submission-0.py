class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)

        # dp[i]：以 nums[i] 结尾的最大子数组和
        dp = [0] * n
        dp[0] = nums[0]

        result = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            result = max(result, dp[i])

        return result