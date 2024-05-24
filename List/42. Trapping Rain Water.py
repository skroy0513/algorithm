from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        water = 0
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        return water

    def trap2(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                water += distance * waters

            stack.append(i)
        return water

Solution().trap2([0,1,0,2,1,0,1,3,2,1,2,1])