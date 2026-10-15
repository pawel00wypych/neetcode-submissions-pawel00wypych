class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False

        stack = []
        i = 0

        while i < len(s):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            elif s[i] == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif s[i] == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif s[i] == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False   
            i += 1

        return len(stack) == 0