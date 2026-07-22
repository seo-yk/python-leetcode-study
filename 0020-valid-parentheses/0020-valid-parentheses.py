class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)

            if c in ")}]":

                if not stack:
                    return False
                
                if pair[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return  len(stack) == 0
