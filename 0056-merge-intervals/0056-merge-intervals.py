class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        ans = [sorted_intervals[0]]
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]

        for cur in sorted_intervals:
            target = ans.pop()
            if target[1] >= cur[0]:
                ans.append([min(target[0], cur[0]), max(target[1], cur[1])])
            else:
                ans.append(target)
                ans.append(cur)

        return ans