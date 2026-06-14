class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        for i in range(len(sentence1)):
            pair1 = [sentence1[i], sentence2[i]]
            pair2 = [sentence2[i], sentence1[i]]
            if (sentence1[i] != sentence2[i] and 
                (pair1 not in similarPairs and
                 pair2 not in similarPairs
                )):
                return False
        return True