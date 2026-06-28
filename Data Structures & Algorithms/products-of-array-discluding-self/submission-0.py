from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 第一遍：res[i] 存 nums[i] 左边所有数的乘积
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # 第二遍：乘上 nums[i] 右边所有数的乘积
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res



        
        