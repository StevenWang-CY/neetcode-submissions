from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        empty_dict = defaultdict(int)

        for num in nums:
            empty_dict[num] += 1

        sorted_list = sorted(empty_dict.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_list[i][0])

        return res
        