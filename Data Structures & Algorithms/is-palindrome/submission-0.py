class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < len(s)/ 2:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            elif s[i].isalnum() and not s[j].isalnum():
                j -= 1
            elif not s[i].isalnum() and s[j].isalnum():
                i += 1
            else:
                i += 1
                j -= 1
                
        return True