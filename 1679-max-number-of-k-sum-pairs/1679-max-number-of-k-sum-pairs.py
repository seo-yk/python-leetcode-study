class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        s_nums = sorted(nums)
        left = 0
        right = len(s_nums)-1

        while left < right:
            target = k - s_nums[right]
            if target > 0:
                if s_nums[left] == target:
                    left += 1
                    right -= 1
                    count += 1
                elif s_nums[left] < target:
                    left += 1
                else: right -= 1
            else:
                right -= 1

        return count