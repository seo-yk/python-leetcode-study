class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                max_count += 1

        left = 1
        right = left + k - 1

        count = max_count
        while right < len(s):
            if s[left-1] in vowels:
                count -= 1

            if s[right] in vowels:
                count += 1

            max_count = max(max_count, count)
            left += 1
            right += 1

        return max_count