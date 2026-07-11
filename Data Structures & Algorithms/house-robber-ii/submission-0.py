class Solution:
    def rob(self, nums: list[int]) -> int:
        # 只有一间房时，直接偷这一间
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses: list[int]) -> int:
            prev2 = 0
            prev1 = 0

            for money in houses:
                current = max(
                    prev1,          # 不偷当前房子
                    prev2 + money   # 偷当前房子
                )

                prev2 = prev1
                prev1 = current

            return prev1

        return max(
            rob_line(nums[:-1]),  # 不考虑最后一间
            rob_line(nums[1:])    # 不考虑第一间
        )