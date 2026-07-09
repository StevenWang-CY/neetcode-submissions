from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                # 去重：同一层里，相同数字只允许作为第一个选择出现
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # 剪枝
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # i + 1，因为每个元素只能用一次
                backtrack(i + 1, remaining - candidates[i])

                path.pop()

        backtrack(0, target)
        return res