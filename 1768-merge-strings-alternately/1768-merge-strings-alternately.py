class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]

        return ans