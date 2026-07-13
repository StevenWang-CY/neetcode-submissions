from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # 总和为奇数，不可能平均分成两个整数和相等的子集
        if total % 2 == 1:
            return False

        target = total // 2

        # dp[j] 表示是否可以选出一些数字，使它们的和为 j
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # 倒序遍历，保证每个数字只能使用一次
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]