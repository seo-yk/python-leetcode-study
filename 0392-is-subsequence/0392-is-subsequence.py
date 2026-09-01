class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        sp = 0
        tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            elif tp < len(t):
                tp += 1

        if sp == len(s):
            return True
        else:
            return False