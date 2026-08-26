class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = []
        max_length = 0

        for i in range(len(s)):
            if s[i] in ans:
                index = ans.index(s[i])
                ans = ans[index+1:]

            ans.append(s[i])
            max_length = max(max_length, len(ans))

        return max_length