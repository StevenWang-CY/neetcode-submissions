class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            # 当前 path 本身就是一个合法子集
            res.append(path[:])

            # 从 start 开始继续选择后面的数字
            for i in range(start, len(nums)):
                path.append(nums[i])      # 选择 nums[i]
                backtrack(i + 1)          # 继续往后选
                path.pop()             # 撤销选择

        backtrack(0)
        return res