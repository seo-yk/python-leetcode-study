class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answer = []

        def solve(start, curr_sum, path):
            if curr_sum == target:
                answer.append(path[:])
                return

            for i in range(start, len(candidates)):
                if curr_sum + candidates[i] <= target:
                    path.append(candidates[i])
                    solve(i, curr_sum + candidates[i], path)
                    path.pop()

        solve(0, 0, [])
        return answer