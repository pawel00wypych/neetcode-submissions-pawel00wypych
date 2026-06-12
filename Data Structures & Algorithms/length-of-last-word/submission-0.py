class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_l = 0
        new_word_l = 0
        for c in s:
            if c == ' ':
                print(f"last_word_l = {last_word_l} new_word_l = {new_word_l}")
                if new_word_l > 0:
                    last_word_l = new_word_l
                new_word_l = 0
            else:
                new_word_l += 1
        if new_word_l > 0:
           last_word_l =  new_word_l
        return last_word_l