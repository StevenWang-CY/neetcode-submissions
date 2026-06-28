from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token in ops:
                b = stack.pop()          # 第二个操作数(先弹出的是右操作数)
                a = stack.pop()          # 第一个操作数
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # "/"
                    stack.append(int(a / b))   # 向零截断,不能用 a // b
            else:
                stack.append(int(token))

        return stack[0]