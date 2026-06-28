from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 按位置从大到小(越靠近终点越先处理)
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        cur_time = 0.0          # 当前最前方车队到达终点的时间

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > cur_time:
                # 追不上前方车队 → 自成新车队
                fleets += 1
                cur_time = time
            # else: time <= cur_time,会被前方车队吸收,不计数

        return fleets