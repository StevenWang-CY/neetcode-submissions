class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # 跳过重复的 left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # 跳过重复的 right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res