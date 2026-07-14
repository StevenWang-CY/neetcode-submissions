from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 从最低位向最高位遍历
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # 当前位加一后不会产生进位
                digits[i] += 1
                return digits

            # 当前位是 9，加一后变成 0，并继续向前进位
            digits[i] = 0

        # 能执行到这里，说明原数组中的所有数字都是 9
        return [1] + digits