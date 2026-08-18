class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        half = len(nums) // 2
        a = self.sortArray(nums[:half])
        b = self.sortArray(nums[half:])

        def combine(A, B):

            p1, p2 = 0, 0
            result = []

            while p1 < len(A) and p2 < len(B):
                if A[p1] <= B[p2]:
                    result.append(A[p1])
                    p1 += 1
                else:
                    result.append(B[p2])
                    p2 += 1

            result.extend(A[p1:])
            result.extend(B[p2:])

            return result

        return combine(a, b)