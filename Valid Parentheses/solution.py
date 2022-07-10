class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        maps = {')' : '(', '}' : '{', ']' : '['}

        for i in s:
            if i in maps:
                if stack:
                    top = stack.pop()
                    if maps[i] != top:
                        return False
                else:
                    return False
            else:
                stack.append(i)

        return not stack
