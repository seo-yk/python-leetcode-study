class Solution:
    def simplifyPath(self, path: str) -> str:
        clean_list = [x for x in path.split("/") if x]
        stack = []

        for word in clean_list:
            if word == '..':
                if stack:
                    stack.pop()
            elif word == '.':
                pass
            else:
                stack.append(word)

        return "/" + "/".join(stack)    