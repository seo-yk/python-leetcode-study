class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        answer = []

        def helper(i, path):
            if i == len(s):
                return answer.append("".join(path))

            if s[i].isdigit():
                path.append(s[i])
                helper(i+1, path)
                path.pop()
            
            else:
                path.append(s[i].lower())
                helper(i+1, path)
                path.pop()
                
                path.append(s[i].upper())
                helper(i+1, path)
                path.pop()

        helper(0, [])
        return answer