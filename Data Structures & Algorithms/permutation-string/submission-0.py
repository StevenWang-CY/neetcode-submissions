class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        s2_window_dict = defaultdict(int)

        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False

        for s in s1:
            s1_dict[s] += 1
        
        for right in range(len_s2):
            s2_window_dict[s2[right]] += 1
            if right >= len_s1:
                s2_window_dict[s2[right - len_s1]] -= 1
            if s2_window_dict[s2[right - len_s1]] == 0:
                del s2_window_dict[s2[right - len_s1]]
            if s1_dict == s2_window_dict:
                return True
        return False
        