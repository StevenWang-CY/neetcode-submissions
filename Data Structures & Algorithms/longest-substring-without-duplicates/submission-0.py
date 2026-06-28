class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        curr_len = 0
        left = 0

        if len(s) == 0:
            return 0

        for lt in s:
            while lt in seen:
                seen.remove(s[left])
                left += 1
                curr_len -=1

            curr_len += 1
            max_len = max(max_len, curr_len)

            seen.add(lt)
        
        return max_len



        