class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        s_nums = sorted(nums)
        left = 0

        while s_nums:
            target = k - s_nums.pop()
            for i in range(left, len(s_nums)):
                if s_nums[i] == target:
                    count += 1
                    left = i+1
                    break
                elif s_nums[i] > target:
                    break
        return count