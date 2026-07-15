class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # 特殊情况
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        # 存储结果
        result = [0] * (m + n)

        # 从个位开始乘
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                # 当前已有值
                total = product + result[i+j+1]

                # 当前位
                result[i+j+1] = total % 10

                # 进位
                result[i+j] += total // 10


        # 去掉最高位0
        ans = ""

        for x in result:
            if not (ans == "" and x == 0):
                ans += str(x)

        return ans