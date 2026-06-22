class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        def is_substring(check: str, word: str) -> bool:
            if len(check) > len(word):
                return False
            i = 0
            j = 0
            substring = ''
            print(f"{check} and {word}")
            while i < len(check) and j < len(word):
                while i < len(check) and j < len(word) and word[j] == check[i]:
                    print(f"substring = {substring} i = {i} j = {j}")
                    substring += word[j]
                    i += 1
                    j += 1
                i = 0
                substring = ''
                j += 1
                
            if i != len(check):
                return False
            return substring == check

        substrings = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j]:
                    #if is_substring(words[i], words[j]):
                    if words[i] in words[j]:
                        substrings.append(words[i])
                        break
        return substrings

