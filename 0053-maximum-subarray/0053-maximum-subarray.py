class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 카다네 알고리즘
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        for i in range(len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])

        return max(dp)