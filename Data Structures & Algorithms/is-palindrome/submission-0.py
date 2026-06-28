from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # 跳过左边非字母数字字符
            while left < right and not s[left].isalnum():
                left += 1

            # 跳过右边非字母数字字符
            while left < right and not s[right].isalnum():
                right -= 1

            # 比较小写后的字符
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True