import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # 最大的石头
            x = -heapq.heappop(heap)  # 第二大的石头

            if x != y:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0