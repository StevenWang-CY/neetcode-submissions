from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # 存下标，保证 nums[q[0]] 是当前窗口最大值
        res = []

        for i in range(len(nums)):
            # 1. 删除滑出窗口的下标
            if q and q[0] < i - k + 1:
                q.popleft()

            # 2. 删除比当前元素小或等于当前元素的队尾
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # 3. 当前下标入队
            q.append(i)

            # 4. 窗口形成后，记录最大值
            if i >= k - 1:
                res.append(nums[q[0]])

        return res