class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)

            if c == ")":
                if not stack or stack.pop() != "(":
                    return False

            if c == "]":
                if not stack or stack.pop() != "[":
                    return False

            if c == "}":
                if not stack or stack.pop() != "{":
                    return False


        return not stack
        