from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        need_count = len(need)
        have = 0

        left = 0
        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            # 如果 c 是 t 需要的字符，并且数量刚好达到要求
            if c in need and window[c] == need[c]:
                have += 1

            # 当窗口已经满足要求，开始收缩左边
            while have == need_count:
                current_len = right - left + 1

                if current_len < best_len:
                    best_len = current_len
                    best_start = left

                # 准备移除左边字符
                left_char = s[left]
                window[left_char] -= 1

                # 如果移除后导致某个需要的字符不够了
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start : best_start + best_len]