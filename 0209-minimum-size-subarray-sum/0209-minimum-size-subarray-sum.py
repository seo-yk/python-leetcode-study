class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        # 브루트 포스
        min_len = float('inf')

        for i in range(len(nums)):
            cur = nums[i]
            cur_len = 1

            if cur >= target:
                return 1

            for j in range(i+1, len(nums)):
                cur = cur + nums[j]
                cur_len = cur_len + 1
                
                if cur >= target:
                    min_len = min(min_len, cur_len)
                    break

        return min_len if min_len != float('inf') else 0
        """

        # 투 포인터
        """
        left = 0
        cur_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            cur_sum = cur_sum + nums[right]
            
            if cur_sum >= target:
                min_len = min(min_len, right-left+1)

                for left in range(left, right):
                    cur_sum -= nums[left]
                    left += 1

                    if cur_sum >= target:
                        min_len = min(min_len, right-left+1)
                    else:
                        break
        
        return min_len if min_len != float('inf') else 0
        """

        # While문
        left = 0
        min_len = float('inf')
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            if cur_sum >= target:
                while cur_sum - nums[left] >= target:
                    cur_sum -= nums[left]
                    left += 1
                min_len = min(min_len, right - left +1)
        return min_len if min_len != float('inf') else 0    