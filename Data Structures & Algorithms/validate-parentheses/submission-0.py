class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{',']': '['}

        for ch in s:

            if ch in '({[':
                stack.append(ch)

            else:
                # if stack empty -> no matching opening
                if not stack:
                    return False

                # check if top matches
                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

        # valid if nothing left
        return len(stack) == 0