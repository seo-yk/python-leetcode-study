class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = left + 1
        can_flip = k
        max_length = 0

        if nums[left] == 0:
            can_flip -= 1

        while right < len(nums):

            if can_flip < 0:
                left += 1
                can_flip = k

            if can_flip == 0 and nums[right] == 0:
                max_length = max(max_length, right - left)
                while nums[left] != 0:
                    left += 1
                left += 1
                can_flip += 1
                continue

            if nums[right] == 0:
                can_flip -= 1
            right += 1

        if can_flip >= 0:
            max_length = max(max_length, right - left)

        return max_length