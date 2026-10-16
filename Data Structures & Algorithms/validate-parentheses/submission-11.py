class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False

        stack = []
        closingToOpen = {'}':'{', ']':'[', ')':'('}
        for l in s:
            if l not in closingToOpen:
                stack.append(l)
            else:
                if len(stack) == 0 or closingToOpen[l] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return True if len(stack) == 0 else False