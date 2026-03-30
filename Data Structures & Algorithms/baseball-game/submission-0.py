class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for op in operations:
            if op == 'D':
                res.append(res[-1] * 2)
            elif op == 'C':
                res.pop()
            elif op =='+':
                res.append(res[-2] + res[-1])
            else:
                res.append(int(op))

        return sum(res)