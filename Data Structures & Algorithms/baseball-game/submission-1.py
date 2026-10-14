class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for o in operations:
            if o == 'D':
                scores.append((scores[-1]) * 2)
            elif o == '+':
                scores.append(int(scores[-1]) + int(scores[-2]))
            elif o == 'C':
                scores.pop()
            else:
                scores.append(int(o))
        return sum(scores)