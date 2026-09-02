class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")" : "(", "]" : "[", "}": "{"}

        for c in s:
            # it appends opening brackets
            if c not in close_to_open:
                stack.append(c)
                continue
            
            # if the top of stack matches the hashmap then we can pop the       opening bracket
            if not stack or stack[-1] != close_to_open[c]:
                return False
            stack.pop()

        return len(stack) == 0
        