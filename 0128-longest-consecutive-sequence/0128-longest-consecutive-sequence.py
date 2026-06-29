# [128] https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ complexity
            - requirement: O(n) --> 정렬 X

            1. set(nums)로 중복 제거
            2. 순회하면서 x-1 값이 있는지 체크 --> 없으면 시작점
            3. current = x
               count = 1
               while(current+1 in set(nums))
                current += 1
                coutn += 1
        """

        sn = set(nums)
        longest = 0

        for x in sn:
            if x-1 not in sn:
                current = x
                count = 1
                
                while(current+1 in sn):
                    current += 1
                    count += 1
                
                longest = max(count, longest)

        return longest