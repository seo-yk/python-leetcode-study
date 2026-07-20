class Solution:
    def climbStairs(self, n: int) -> int:
        # 반복문
        """
        if n <= 2:
            return n

        prev1 = 1       #1전 값
        prev2 = 2       #2전 값
        current = 0
        
        for _ in range(n-2):
            current = prev1+prev2
            prev2 = prev1
            prev1 = current

        return current
        """

        # dp
        dp = []

        # dp[n] = dp[n-1] + dp[n-2]
        for i in range(n+1):
            if(i<=2):
                dp.append(i)
            else:
                dp.append(dp[i-1]+dp[i-2])

        return dp[n]
