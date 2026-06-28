class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = list(set(nums))
        num_set.sort()
        if len(nums) == 0:
            return 0
        res = 1
        curr = 1
        prev = num_set[0]
        for num in num_set[1:]:
            if num == prev + 1:
                curr += 1
                if curr > res:
                    res = curr
            else:
                curr = 1
            prev = num
        return res

        