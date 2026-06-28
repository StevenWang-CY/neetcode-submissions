from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n          # 默认全 0:没等到更暖的就是 0
        stack = []                # 存下标,栈内对应的温度从栈底到栈顶递减

        for i in range(n):
            # 今天比栈顶那天暖 → 把栈顶那天结算掉
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result