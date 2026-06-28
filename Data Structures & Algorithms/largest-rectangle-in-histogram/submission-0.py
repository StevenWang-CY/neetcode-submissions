class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # 存下标，保证 heights[stack] 单调递增
        max_area = 0

        # 加一个 0，强制结算栈中剩余柱子
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                idx = stack.pop()
                height = heights[idx]

                # 左边第一个比 height 小的位置
                left = stack[-1] if stack else -1

                # 右边第一个比 height 小的位置就是当前 i
                right = i

                width = right - left - 1
                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area