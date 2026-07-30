class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 2):

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1
            cur = sorted_nums[i]

            while left < right:
                target = 0 - cur
                if sorted_nums[left] + sorted_nums[right] == target:
                    ans.append([cur, sorted_nums[left], sorted_nums[right]])

                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1

                    left += 1
                    right -= 1

                elif sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return ans