class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        md = collections.Counter(magazine)
        rd = collections.Counter(ransomNote)
        
        return not (rd - md)

        