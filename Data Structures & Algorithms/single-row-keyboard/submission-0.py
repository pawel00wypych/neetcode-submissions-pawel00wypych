class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_dict = {}
        for i in range(len(keyboard)):
            keyboard_dict[keyboard[i]] = i
        total_time = 0
        for i in range(len(word)):
            if i == 0:
                total_time += keyboard_dict[word[i]]
            else:
                total_time += abs(keyboard_dict[word[i-1]] - keyboard_dict[word[i]])
        return total_time