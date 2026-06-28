class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        for right in range(len_s2):
            # 右边字符进入窗口
            window_count[ord(s2[right]) - ord('a')] += 1

            # 如果窗口长度超过 len_s1，左边字符移出窗口
            if right >= len_s1:
                left_char = s2[right - len_s1]
                window_count[ord(left_char) - ord('a')] -= 1

            # 窗口长度达到 len_s1 时比较
            if right >= len_s1 - 1:
                if window_count == s1_count:
                    return True

        return False
            
        