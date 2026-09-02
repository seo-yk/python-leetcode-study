class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = left + k

        max_sum = 0
        for i in range(left, right):
            max_sum += nums[i]

        sum = max_sum
        while right < len(nums):
            sum = sum - nums[left] + nums[right]
            max_sum = max(max_sum, sum)
            left += 1
            right += 1

        return max_sum / k