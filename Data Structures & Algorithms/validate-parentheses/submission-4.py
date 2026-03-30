class Solution:
    def is_it_closing_b(self, c: str) -> bool:
        if c in [')',']','}']:
            return True
        else:
            return False

    def return_opening_b(self, c:str) -> str:
        if c == ')':
            return '('
        elif c == '}':
            return '{'
        elif c == ']':
            return '['

    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        char_stack = []    
        for i in range(len(s)):
            if self.is_it_closing_b(s[i]) is False:
                char_stack.append(s[i])
            else:
                if len(char_stack) == 0:
                    return False

                c = char_stack.pop()
                if c != self.return_opening_b(s[i]):
                    return False

        if len(char_stack) == 0:
            return True
        else:
            return False