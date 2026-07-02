from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                # mid 速度已经够快了
                # 但我们要找最小速度，所以继续往左找
                right = mid
            else:
                # mid 太慢了，需要更快
                left = mid + 1

        return left