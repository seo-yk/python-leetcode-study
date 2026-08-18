class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        s = set(a+b)
        ans = []
        for item in s:
            if nums.count(item) > len(nums) // 3:
                ans.append(item)
        return ans