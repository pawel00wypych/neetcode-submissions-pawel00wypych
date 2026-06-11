class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        duplicates = {}
        for i in range(len(s)):
            duplicates[s[i]] = duplicates.get(s[i], 0) + 1
            duplicates[t[i]] = duplicates.get(t[i], 0) - 1

        for v in duplicates.values():
            if v != 0:
                return False
        return True