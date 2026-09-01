class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water = 0

        while left < right:
            w = right - left
            h = min(height[right], height[left])
            max_water = max(max_water, w * h)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_water