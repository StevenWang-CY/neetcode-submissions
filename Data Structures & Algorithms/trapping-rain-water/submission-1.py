class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()

                # 如果没有左边界，就不能接水
                if not stack:
                    break

                left = stack[-1]
                right = i

                width = right - left - 1
                bounded_height = min(height[left], height[right]) - height[bottom]

                ans += width * bounded_height

            stack.append(i)

        return ans