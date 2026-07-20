class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = []
        
        # dp[n] = max(dp[n-2]+nums[n], dp[n-1])
        for i, num in enumerate(nums):
            if i==0:
                dp.append(nums[0]) 
            elif i==1:
                dp.append(max(nums[0], nums[1]))
            else:
                dp.append(max(dp[i-2]+num, dp[i-1]))

        return dp[len(dp)-1]