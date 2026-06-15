from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letters = Counter(s)
        unique_items = 0

        for k, v in letters.items():
            if v%2 == 1 and unique_items < 1:
                unique_items += 1
            elif v%2 != 0:
                return False 
        return True